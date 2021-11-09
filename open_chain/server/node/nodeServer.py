from socketserver import ThreadingTCPServer
from requestHandler import RequestHandler

DEFAULT_NODE_HOST = '0.0.0.0'
DEFAULT_NODE_PORT = 1776

# serve the node to node comms, at socket level
class NodeServer(ThreadingTCPServer):
  def __init__(self):
    self.server_address = (DEFAULT_NODE_HOST, DEFAULT_NODE_PORT)
    self.RequestHandlerClass = RequestHandler
    self.is_running = False

  def is_running(self):
    return self.is_running

  def start(self):
    self.serve_forever()
    self.is_running = True
  
  def stop(self):
    self.shutdown()
    self.is_running = False
