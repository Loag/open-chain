# serve the application interface http
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
DEFAULT_APP_HOST = '0.0.0.0'
DEFAULT_APP_PORT = 1783
CONTENT_TYPE = 'application/json'

class HTTPRequestHandler(BaseHTTPRequestHandler):
  def _set_headers(self, success=True):
      self.send_response(200 if success else 500)
      self.send_header('Content-type', CONTENT_TYPE)
      self.end_headers()

  def do_GET(self):
      self._set_headers()
      self.wfile.write("received get request")
      
  def do_POST(self):
      '''Reads post request body'''
      self._set_headers()
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      self.wfile.write("received post request:<br>{}".format(post_body))

class AppServer(ThreadingHTTPServer):
  def __init__(self):
    self.server_address = (DEFAULT_APP_HOST, DEFAULT_APP_PORT)
    self.RequestHandlerClass = HTTPRequestHandler
    self.is_running = False
  
  def start(self):
    self.serve_forever()
    self.is_running = True
  
  def stop(self):
    self.shutdown()
    self.is_running = False
