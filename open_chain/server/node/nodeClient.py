from socket import socket
import threading

# get the available nodes it knows about here and ping them..?
class NodeClient:
  def __init__(self, host, port=1776):
    self.socket = socket()
    self.host = host
    self.port = port

  def connect(self):
    self.socket.connect((self.host, self.port))

  def send(self, data):
    pass

  def close(self):
    self.socket.close()
  
  '''
    Message is an encoded string
    
    Example:

      HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
      bytes = str.encode(HTTPMessage)
  '''
  def send(self, message):
    self.socket.sendall(message)
    self.__receive()

  def __receive(self):
    while True:

      res = self.socket.recv(1024)

      if not res:
        break

    self.close()

  def Connect2Server():

      # Send a message to the web server to supply a page as given by Host param of GET request

      HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"

      bytes       = str.encode(HTTPMessage)

      socketObject.sendall(bytes)

      # Receive the data

      while(True):

          data = socketObject.recv(1024)

          print(data)

          if(data==b''):

              print("Connection closed")

              break

      socketObject.close()

  print("Client - Main thread started")  

  ThreadList  = []

  ThreadCount = 20

  for index in range(ThreadCount):

      ThreadInstance = threading.Thread(target=Connect2Server())

      ThreadList.append(ThreadInstance)

      ThreadInstance.start()

  # Main thread to wait till all connection threads are complete

  for index in range(ThreadCount):

      ThreadList[index].join()