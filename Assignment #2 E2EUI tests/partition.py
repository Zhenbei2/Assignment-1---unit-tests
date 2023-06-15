from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from solution import Solution

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        string = data['string']
        solution = Solution()
        res = solution.partitionLabels(string)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(res).encode())

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
