#!/usr/bin/env python

print 'Content-type: text/html \n'

from os.path import join, abspath
import cgi, sha, sys

BASE_DIR = abspath('../../../home/yuzhipeng/data')

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password') 


if not (filename and text and password):  
    print('Invalid parameters')  
    sys.exit()  

if sha.sha(password).hexdigest() != 'd033e22ae348aeb5660fc2140aec35850c4da997':  
    print('Invalid password')  
    sys.exit()  

print "1"
print join(BASE_DIR, filename)
try:
    f = open(join(BASE_DIR, filename), 'w')
except Exception as err:
    print err  
print "1"
f.write(text)  
print "2"
f.close()  
  
print('The file has been saved.') 
