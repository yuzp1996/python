import socket, select
"""
The Service with select
"""
s = socket.socket()

host = socket.gethostname()
port = 1024
s.bind((host,port))

s.listen(5)
inputs =[s]
while True:
    rs, ws, es = select.select(inputs, [], [])
# parameter means (input,output,exception) 
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print 'Got connect from ', addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)
            else:
                print data
