#encoding=utf-8

import wx
import telnetlib
from time import sleep
import thread
class Client(wx.App):
    def _init_(self):
        super(Client,self).__init__()
    def OnInit(self):
        self.win = win = wx.Frame(None,title="Connect",size=(400,120))
        bkg = wx.Panel(win)
        loadButton = wx.Button(bkg, label='Connect',size=(100,30))
        loadButton.Bind(wx.EVT_BUTTON, self.OnSend)
        str1 = wx.StaticText(bkg, label="IP地址")
        self.filename = filename = wx.TextCtrl(bkg)
        str2 = wx.StaticText(bkg, label="用户名")
        self.contents = contents = wx.TextCtrl(bkg)


        hbox = wx.BoxSizer()
        hbox.Add(str1,proportion=0,flag=wx.LEFT, border=5)
        hbox.Add(filename, proportion=1, flag=wx.EXPAND)
        # hbox.Add(loadButton, proportion=1, flag=wx.LEFT, border=5)

        hbox1 = wx.BoxSizer()
        hbox1.Add(str2,proportion=0,flag=wx.LEFT,border=5)
        hbox1.Add(contents, proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)


        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=1, flag=wx.EXPAND | wx.ALL,border=5 )
        vbox.Add(hbox1,proportion=1, flag=wx.EXPAND | wx.ALL,border=5)
        vbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=270)
        bkg.SetSizer(vbox)


        win.Show()
        return True
    #
    #
    # def ChatRoom(self,event):
    #     self.winChat =winChat= wx.Frame(None,title="ChatRoom",size=(500,500))
    #
    #
    #     bkg = wx.Panel(winChat)
    #     loadButton = wx.Button(bkg, label='Send',size=(100,30))
    #     # loadButton.Bind(wx.EVT_BUTTON, self.OnSend)
    #     cancleButton = wx.Button(bkg, label='Cancle',size=(100,30))
    #     str1 = wx.StaticText(bkg, label="对话框")
    #     self.allInput = allInput = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)
    #     str2 = wx.StaticText(bkg, label="输入对话")
    #     self.Input = Input = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)
    #
    #
    #     hbox = wx.BoxSizer()
    #     hbox.Add(str1,proportion=0,flag=wx.LEFT, border=5)
    #     hbox.Add(allInput, proportion=1, flag=wx.EXPAND)
    #
    #     hbox1 = wx.BoxSizer()
    #     hbox1.Add(str2,proportion=0,flag=wx.LEFT,border=5)
    #     hbox1.Add(Input, proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
    #
    #     hbox2 = wx.BoxSizer()
    #     hbox2.Add(loadButton, proportion=0, flag=wx.LEFT, border=270)
    #     hbox2.Add(cancleButton, proportion=0, flag=wx.LEFT, border=0)
    #
    #     vbox = wx.BoxSizer(wx.VERTICAL)
    #     vbox.Add(hbox, proportion=2, flag=wx.EXPAND | wx.ALL,border=5 )
    #     vbox.Add(hbox1,proportion=1, flag=wx.EXPAND | wx.ALL,border=5)
    #     vbox.Add(hbox2,proportion=0, flag=wx.EXPAND | wx.ALL,border=5)
    #
    #
    #     bkg.SetSizer(vbox)
    #
    #     winChat.Show()
    #
    def OnSend(self, event):

        import telnetlib
        '''''Telnet远程登录：Windows客户端连接Linux服务器'''

        # 连接Telnet服务器
        username = self.contents.GetValue().encode('ascii')   # 登录用户名
        Host = self.filename.GetValue().encode('ascii')
        tn.open(Host, port=5005, timeout = 10)
        tn.set_debuglevel(2)
        tn.read_until('Welcome to TestChat')
        tn.write("login "+username+"\r\n")
        self.win.Close()
        ChatFrame(None, -1, title = 'Yuzhipeng Chat Room', size = (500, 350))




class ChatFrame(wx.Frame):
    """
    聊天窗口
    """

    def __init__(self, parent, id, title, size):
        '初始化，添加控件并绑定事件'
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)
        self.Center()
        self.chatFrame = wx.TextCtrl(self, pos = (5, 5), size = (490, 310), style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.message = wx.TextCtrl(self, pos = (5, 320), size = (300, 25))
        self.sendButton = wx.Button(self, label = "Send", pos = (310, 320), size = (58, 25))
        self.usersButton = wx.Button(self, label = "Users", pos = (373, 320), size = (58, 25))
        self.closeButton = wx.Button(self, label = "Close", pos = (436, 320), size = (58, 25))
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)
        self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
        self.closeButton.Bind(wx.EVT_BUTTON, self.close)
        self.chatFrame.SetValue("Welcome to Yuzhipeng's ChatRoom! \r\n")
        thread.start_new_thread(self.receive, ())
        self.Show()

    def send(self, event):
        '发送消息'
        message = str(self.message.GetLineText(0)).strip()
        if message != '':
            tn.write(message + '\r\n')
            self.message.Clear()
            # self.chatFrame.AppendText('me: '+message+'\n')

    def lookUsers(self, event):
        '查看当前在线用户'
        tn.write('look\n')

    def close(self, event):
        '关闭窗口'
    	tn.write('logout\n')
    	tn.close()
    	self.Close()

    def receive(self):
        '接受服务器的消息'
        while True:
        	sleep(0.1)
        	result = tn.read_very_eager()
        	if result != '':
        		self.chatFrame.AppendText(result)


def main():

    client = Client()
    client.MainLoop()

if __name__ == '__main__':
    finish = ':~$ '      # 命令提示符
    #123.207.153.155
    tn = telnetlib.Telnet()
    main()
