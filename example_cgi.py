import http.server

PORT = 8000


class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi']


with http.server.HTTPServer(("",PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
