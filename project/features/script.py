import http.server
import socketserver
import db.db_operations
from urllib.parse import urlparse, parse_qs
from features.blocking_operations import unblock_entry

PORT = 80


class MaliciousHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith('/unblock'):
            parsed_url = urlparse(self.path)
            params = parse_qs(parsed_url.query)
            url_param = params.get('url', [''])[0].replace('http://', '').rstrip('/')
            if url_param:
                self.unblock(url_param)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Unblocked')
                return
        else:
            self.send_response(200)
            self.end_headers()
            with open('project\\features\\index.html', 'rb') as file:
                self.wfile.write(file.read())

    def unblock(self, url):
        target_data = db.db_operations.custom_query(
            f'select url, data_type, operation_time, current_status from blocked_data where url = "{url}"')[0]

        if target_data:
            unblock_entry(target_data)


with socketserver.TCPServer(("", PORT), MaliciousHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
