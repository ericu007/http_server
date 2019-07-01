import http.server   # 응답 대응
import socketserver  # 실제 응답

PORT = 8000

# 기본: 80
# 443

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
