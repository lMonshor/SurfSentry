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
path_index_html = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\assets' ,'index.html')
httpd = None

class MaliciousHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
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
        target_data = db.db_operations.custom_query(
            f'select url, data_type, operation_time, current_status from blocked_data where url = "{url}"')

        if target_data:
            target_data = target_data[0]
            blocking_operations.unblock_entry(target_data)

def start_server():
    global server_running, httpd
    if not server_running:
        httpd = socketserver.TCPServer((IP, PORT), MaliciousHandler)
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server_running = True
        print(f"Serving at port {PORT}")

def stop_server():
    global server_running, httpd
    if httpd:
        httpd.shutdown()
        httpd.server_close()
        server_running = False
        print("Server stopped")
