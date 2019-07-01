from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import requests
from bs4 import BeautifulSoup
import html as mht

PORT = 8000


class Handler(BaseHTTPRequestHandler):
    """
    get, post, url, delete, head
    """
    def do_GET(self):
        """
        시작줄
        헤더
        본문
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        query_text = urlparse(self.path).query
        queries = parse_qs(query_text)
        message = "Hello"
        if "name" in queries:
            message += queries['name'][0]

        message += """
            <form action="" method="post">
                <input type="text" name="search">
                <input type="submit" value="Search">
            </form>
        """
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_length)
        queries = parse_qs(post_body.decode('utf8'))
        query = mht.unescape(queries['search'][0])
        url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="+query
        req = requests.get(url)

        if req.status_code == requests.codes.ok:
            print("접속 성공")
            html = BeautifulSoup(req.text, "html.parser")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(str(html), 'utf8'))
        return


def run():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, Handler)
    print("serving at port", PORT)
    httpd.serve_forever()


run()
