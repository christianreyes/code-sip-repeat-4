# adapted from https://anshu-dev.medium.com/creating-a-python-web-server-from-basic-to-advanced-449fcb38e93b

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import parse_qs

import csr_password_gen

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # process the GET HTTP request
    def do_GET(self):
        parsed_querystring = urlparse(self.path) # parse the data from the URL

        if parsed_querystring.path == '/': # serve index page if path is /
            self.path = '/index.html'
        try:
            page_contents = open(self.path[1:]).read() # read contents of file
            if parsed_querystring.query != '': # if query string in url
                # get complexity string
                complexity_string = parse_qs(parsed_querystring.query)["complexity_string"][0]

                # generate random password using that complexity string
                random_generated_password = csr_password_gen.generate_complex_password(complexity_string) 

                # replace the password template in the html with the generated value
                page_contents = page_contents.replace("{{ password }}", random_generated_password)

            self.send_response(200) # HTTP code OK
            self.send_header('Content-type', 'text/html') # tell client to expect html text
            self.end_headers()
            self.wfile.write(bytes(page_contents, 'utf-8')) # write to contents to the connection
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
