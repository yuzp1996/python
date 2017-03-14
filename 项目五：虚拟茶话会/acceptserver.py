from asyncore import dispatcher
import socket, asyncore

class ChatServer(dispatcher):

    def handle_accept(self):
        conn, addr = self.accept() # return a connection and a address
        print 'Connection atttempt from ', addr[0]

s = ChatServer()
s.create_socket(socket.AF_INET, socket.SOCK_STREAM) #identify the type of the socket 
s.bind(('', 5005))
s.listen(6)
asyncore.loop() #loop
