from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 解析请求参数
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_post_data = urllib.parse.parse_qs(post_data)
        string = parsed_post_data['string'][0] if 'string' in parsed_post_data else ''

        # 调用分割字符串的函数
        result = partition_string(string)

        # 设置HTTP响应状态码和内容类型
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # 发送响应结果
        self.wfile.write(str(result).encode())

def partition_string(string):
    # 分割字符串的逻辑
    count = {}
    res = []
    i, length = 0, len(string)
    for j in range(length):
        c = string[j]
        count[c] = j

    curLen = 0
    goal = 0
    while i < length:
        c = string[i]
        goal = max(goal, count[c])
        curLen += 1

        if goal == i:
            res.append(curLen)
            curLen = 0
        i += 1

    return ','.join(map(str, res))

def start_server():
    host = 'localhost'
    port = 8000
    server = HTTPServer((host, port), MyHandler)
    print(f"Server started at http://{host}:{port}")
    server.serve_forever()

if __name__ == '__main__':
    start_server()
