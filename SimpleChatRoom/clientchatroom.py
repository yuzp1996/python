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
        str1 = wx.StaticText(bkg, label="IP地址: ")
        self.filename = filename = wx.TextCtrl(bkg)
        str2 = wx.StaticText(bkg, label="用户名: ")
        self.contents = contents = wx.TextCtrl(bkg)


        hbox = wx.BoxSizer()
        hbox.Add(str1,proportion=0,flag=wx.LEFT, border=5)
        hbox.Add(filename, proportion=1, flag=wx.EXPAND)

        hbox1 = wx.BoxSizer()
        hbox1.Add(str2,proportion=0,flag=wx.LEFT,border=5)
        hbox1.Add(contents, proportion=1,flag=wx.EXPAND)


        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=1, flag=wx.EXPAND | wx.ALL,border=5 )
        vbox.Add(hbox1,proportion=1, flag=wx.EXPAND | wx.ALL,border=5)
        vbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=270)
        bkg.SetSizer(vbox)


        win.Show()
        self.filename.SetValue("123.207.153.155")
        return True

    def OnSend(self, event):

        import telnetlib
        '''''Telnet远程登录：Windows客户端连接Linux服务器'''
        # 连接Telnet服务器
        username = u' '.join(self.contents.GetValue()).encode('utf-8')   # 登录用户名
        Host = self.filename.GetValue().encode('ascii')
        tn.open(Host, port=5005, timeout = 10)
        tn.set_debuglevel(2)
        tn.read_until('Welcome to TestChat')
        tn.write("login "+username+"\r\n")
        self.win.Close()
        ChatFrame(None, -1, title = '鱼狗狗聊天室', size = (540, 360))




class ChatFrame(wx.Frame):
    """
    聊天窗口
    """

    def __init__(self, parent, id, title, size):
        '初始化，添加控件并绑定事件'
        wx.Frame.__init__(self, parent, id, title)

        self.SetSize(size)
        self.Center()
        self.bkg = wx.Panel(self)


        self.chatFrame = chatFrame = wx.TextCtrl(self.bkg, size = (390, 310), style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.manListFrame = manListFrame = wx.TextCtrl(self.bkg, size = (200,310), style = wx.TE_MULTILINE | wx.TE_READONLY)

        # 信息框，绑定回车事件
        self.message = wx.TextCtrl(self.bkg,  size = (300, 25),style = wx.TE_PROCESS_ENTER)
        self.message.Bind(wx.EVT_TEXT_ENTER, self.send, self.message)

        self.sendButton = wx.Button(self.bkg, label = "发送", size = (58, 25))
        self.usersButton = wx.Button(self.bkg, label = "查看用户",  size = (58, 25))
        self.closeButton = wx.Button(self.bkg, label = "关闭", size = (58, 25))
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)
        self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
        self.closeButton.Bind(wx.EVT_BUTTON, self.close)
        self.chatFrame.SetValue("欢迎来到鱼狗狗的聊天室! \r\n")
        self.manListFrame.SetValue("谁在这呢! \r\n")

        hbox = wx.BoxSizer()
        hbox.Add(self.chatFrame, proportion=2, flag=wx.EXPAND, border=1)
        hbox.Add(self.manListFrame, proportion=1, flag=wx.EXPAND, border=1)

        hbox1 = wx.BoxSizer()
        hbox1.Add(self.message, proportion=2, flag=wx.EXPAND, border=1)
        hbox1.Add(self.sendButton, proportion=1,  flag=wx.EXPAND, border=1)
        hbox1.Add(self.usersButton, proportion=1, flag=wx.EXPAND, border=1)
        hbox1.Add(self.closeButton, proportion=1 , flag=wx.EXPAND, border=1)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion = 3, flag=wx.EXPAND | wx.ALL,border=5 )
        vbox.Add(hbox1, proportion = 1, flag=wx.EXPAND | wx.ALL,border=5 )

        self.bkg.SetSizer(vbox)
        thread.start_new_thread(self.receive, ())
        self.Show()
        self.lookUsers(self)

    def send(self, event):
        '发送消息'
        message = u' '.join(self.message.GetLineText(0)).encode('utf-8').strip()
        if message != '':
            tn.write(message + '\r\n')
            self.message.Clear()

    def lookUsers(self, event):
        '查看当前在线用户'
        tn.write('who\r\n')

    def close(self, event):
        '关闭窗口'
    	tn.write('logout\n')
    	tn.close()
    	self.Close()

    def receive(self):
        '接受服务器的消息'
        Separator = "----------------------\r\n"
        while True:
            sleep(0.1)
            result = tn.read_very_eager()
            if result != '':
                # if result.startswith("The fo"):
                #     self.manListFrame.SetValue("谁在这呢! \n"+result[29:])
                # else:
                self.chatFrame.AppendText("-----"+Separator+result+Separator)



def main():

    client = Client()
    client.MainLoop()

if __name__ == '__main__':
    #123.207.153.155
    tn = telnetlib.Telnet()
    main()
