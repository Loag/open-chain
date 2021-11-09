from socketserver import StreamRequestHandler
class RequestHandler(StreamRequestHandler):
  def handle(self):
    # Receive and print the data received from client
    print("Recieved one request from {}".format(self.client_address[0]))
    # this is the data to pass to the app to handle..?
    msg = self.rfile.readline().strip()

