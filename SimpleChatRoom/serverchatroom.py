from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore
import wx

PORT = 5005
NAME = 'TestChat'
class EndSession(Exception):pass

#this is command
class CommandHandler:

    def unknown(self, session, cmd):
        session.push ('Unknown command : %s\r\n' % cmd)

    def handle(self, session, line):
        if not line.strip(): return
        parts = line.split(' ', 1)
        cmd = parts[0]

        if cmd not in [ 'login', 'look', 'logout','who','getout']:
            meth = getattr(self, 'do_say', None)
            meth(session, line)
        else:
            try: line = parts[1].strip()
            except IndexError: line = ''
            meth = getattr(self, 'do_'+cmd, None)
            try:
                meth(session, line)
            except TypeError:
                self.unknown(session, cmd)

# above these are kinds of rooms
class Room(CommandHandler):

    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        self.sessions.append(session)

    def remove(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
             session.push(line)

    def do_logout(self, session, line):
        raise EndSession

class LoginRoom(Room):

    def add(self, session):
        Room.add(self, session)
        self.broadcast("Welcome to %s\r\n"% self.server.name)

    def unknown(self, session, cmd):
        session.push('Please log in \n Use"login <nick>"\r\n')

    def do_login(self, session, line):
        name = line.strip()
        if not name:
            session.push("Please Enter a Name\r\n")
        elif name in self.server.users:
            session.push('The name "%s" is taken.\r\n'% name)
            session.push('Please try again\t\n')
        else:
            session.name = name
            session.push('Welcome to here "%s".\r\n'% name)
            session.enter(self.server.main_room)

class ChatRoom(Room):

    def add(self, session):
        self.broadcast(session.name + ' has enter room \r\n')
        self.server.users[session.name] = session
        Room.add(self, session)
    def remove(self, session):
        Room. remove(self, session)
        self.broadcast(session.name + ' has leave the room \r\n')

    def do_say(self, session, line):
        self.broadcast(session.name+': '+line+'\r\n')

    def do_look(self, session, line):
        session.push('The foolowing are in this room :\r\n')
        for other in self.sessions:
            session.push(other.name + '\r\n')

    def do_who(self, session, line):
        session.push('The following are logged in :\r\n')
        for name in self.server.users:
            session.push(name+'\r\n')

    def do_getout(self, session, line):

        if session.name == 'admin':
            self.broadcast(line + ' has been cleaned \r\n')
            self.server.users[line].handle_close()
        else:
            self.broadcast(session.name+' try to kill other people \r\n')
            session.push('please check your account,you have no right to do it \r\n')


class LogoutRoom(Room):
    def add(self, session):
        try: del self.server.users[session.name]
        except KeyError:
            pass

#above is
class ChatSession(async_chat):
    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    def enter(self, room):
        try: cur = self.room
        except AttributeError: pass
        else: cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)

        self.data = []

        try: self.room.handle(self, line)
        except EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))


# this is the main server
class ChatServer(dispatcher):
    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name =name
        self.users={}
        self.main_room = ChatRoom(self)
    def handle_accept(self):
        conn, addr=self.accept()
        print conn
        print addr
        ChatSession(self, conn)



# The events in the Box
# def wxPythonBox():
#     app = wx.App()
#     win = wx.Frame(None, title = "ChatRoom", size = (410,335))
#     bkg = wx.Panel(win)
#
#     loadButton = wx.Button(bkg, label='send')
#     loadButton.Bind(wx.EVT_BUTTON, send)
#
#     saveButton = wx.Button(bkg, label='cancle')
#     saveButton.Bind(wx.EVT_BUTTON, cancle)
#
#     filename = wx.TextCtrl(bkg)
#
#     contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)
#
#
#
#     hbox = wx.BoxSizer()
#     hbox.Add(filename, proportion=1, flag=wx.EXPAND)
#     hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
#     hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
#
#     vbox = wx.BoxSizer(wx.VERTICAL)
#     vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL,border=5 )
#     vbox.Add(contents, proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
#     bkg.SetSizer(vbox)
#
#     win.Show()
#
#     app.MainLoop()
#
#
# def send(event):
#     print 'load'
#
# def cancle(event):
#     print 'save'


# you can start here
if __name__ == '__main__':

# init the wx box
    # wxPythonBox();
    s = ChatServer(PORT, NAME)
    try: asyncore.loop()
    except KeyboardInterrupt: print
