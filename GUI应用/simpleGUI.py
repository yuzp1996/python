import wx

def hello(event):
    print "HEllo World!"

app = wx.App()

win = wx.Frame(None, title="Hello wxPython",
               size=(200, 100))
button = wx.Button(win, label="niaho",pos=(20,40),size=(100,50))
button.Bind(wx.EVT_BUTTON, hello)
win.Show()
app.MainLoop()
