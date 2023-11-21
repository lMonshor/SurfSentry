import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import threading
import os
import sys
import db.db_operations
from features import blocking_operations

IP = '0.0.0.0'
PORT = 80
server_running = False
path_index_html = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\assets', 'index.html')
httpd = None


class MaliciousHandler(http.server.SimpleHTTPRequestHandler):

    def my_log(self, format, *args):
        pass

    def do_GET(self):
        self.log_message = self.my_log
        if self.path.startswith('/unblock'):
            parsed_url = urlparse(self.path)
            params = parse_qs(parsed_url.query)
            url_param = params.get('url', [''])[0].replace(
                'http://', '').rstrip('/')
            if url_param:
                self.unblock(url_param)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Unblocked')
                return
        else:
            self.send_response(200)
            self.end_headers()
            with open(path_index_html, 'rb') as file:
                self.wfile.write(file.read())

    def unblock(self, url):
        self.log_message = self.my_log
        entry = db.db_operations.get_entry_details(
            column_name='address,data_type',
            address=url)
        if entry:
            blocking_operations.remove_entry(entry=entry)


def start_server():
    global server_running, httpd
    if not server_running:
        httpd = socketserver.TCPServer((IP, PORT), MaliciousHandler)
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server_running = True


def stop_server():
    global server_running, httpd
    if httpd:
        httpd.shutdown()
        httpd.server_close()
        server_running = False
