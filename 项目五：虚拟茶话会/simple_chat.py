from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = 'TestChat'
class ChatSession(async_chat):

	def __init__(self, server, sock):
		Async_Chat.__init__(self, sock)
		self.server = server
		self.set_terminator("\r\n")
		self.data = []
		self.push("Welcome sto %s\r\n" % self.server.name)

	def collect_incoming_data(self, data): # get the news
		self.data.append(data)

	def found_terminator(self): # end the news
		line = ''.join(self.data)
		self.data = []
		self.server.broadcast(line)

	def handle_close(self): # end the connection
		async_chat.handle_close(self)
		self.server.disconnect(self)

class ChatServer(dispatcher):
    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name = name
        self.sessions = []
        
    def disconnect(self, session):
        print "out"
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line+'\r\n')

    def handle_accpet(self):
        conn, addr = self.accept()
        print "connect ffrom "
        self.sessions.append(ChatSession(self, conn))

if __name__=='__main__':
    s = ChatServer(PORT, NAME)
    try: asyncore.loop()
    except KeyboardInterrupt : print		


