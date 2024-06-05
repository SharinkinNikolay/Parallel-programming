
from http.server import BaseHTTPRequestHandler, HTTPServer
import queue

requests = queue.Queue()
results = queue.Queue()

#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #handle GET command
    def do_GET(self):

        if(self.path.startswith("client:")):
            requests.put(self.path[7:])
            self.send_response(200)
            self.send_header('Content-type','text-html')
            self.end_headers()
            self.wfile.write(b'status:OK')

        if(self.path.startswith("worker:")):
            if(requests.empty()):
                self.send_response(200)
                self.send_header('Content-type','text-html')
                self.end_headers()
                self.wfile.write(b'EMPTY')
            else:
                self.send_response(200)
                self.send_header('Content-type','text-html')
                self.end_headers()
                self.wfile.write(requests.get().encode())

        if(self.path.startswith("result:")):
            results.put(self.path[7:])
            self.send_response(200)
            self.send_header('Content-type','text-html')
            self.end_headers()
            self.wfile.write(b'status:OK to worker')

        if(self.path == "checkres"):
            if(results.empty()):
                self.send_response(200)
                self.send_header('Content-type','text-html')
                self.end_headers()
                self.wfile.write(b'EMPTY')
            else:
                self.send_response(200)
                self.send_header('Content-type','text-html')
                self.end_headers()
                self.wfile.write(results.get().encode())
            
    
def run():
    print('http server is starting...')

    #ip and port of servr
    #by default http server port is 80
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()
