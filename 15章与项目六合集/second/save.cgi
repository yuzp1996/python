#!/usr/bin/env python

print 'Content-type: text/html\n'

from os.path import join, abspath
import cgi, sha, sys

BASE_DIR = abspath('data')

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password') 

if not (filename and text and password):  
    print('Invalid parameters')  
    sys.exit()  
  
if hashlib.sha1(password).hexdigest() != 'd033e22ae348aeb5660fc2140aec35850c4da997':  
    #admin的sha1是'7c4a8d09ca3762af61e59520943dc26494f8941b'，判断密码是否正确  
    print('Invalid password')  
    sys.exit()  

f = open(join(BASE_DIR, filename), 'w')  
f.write(text)  
f.close()  
  
print('The file has been saved.') 
