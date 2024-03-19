# adapted from https://anshu-dev.medium.com/creating-a-python-web-server-from-basic-to-advanced-449fcb38e93b

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # process the GET HTTP request
    def do_GET(self):
        if self.path == '/': # if path (URL) is /, serve index.html
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read() # read the path specified
            self.send_response(200) # HTTP code OK
            self.send_header('Content-type', 'text/html') # tell client to expect html text
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8')) # write to contents to the connection
        except: # if any problem with the above, send the 404 error code
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found') # write the text out to the connection for user

def main():
    ip, port = "localhost", 8000 
    httpd = HTTPServer((ip, port), SimpleHTTPRequestHandler) # setup the http server
    httpd.serve_forever() # make web server available at http://localhost:8000/

if __name__ == "__main__":
    main()
