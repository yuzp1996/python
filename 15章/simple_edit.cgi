#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

text = form.getValue('text', open('simple_edit.bat').read())
f = open('simple_edit.dat','w')
f.write(text)
f.close()

print """
Content-type: text/html

<html>
<head>
<title>A Simple Edit</title>
</head>

<body>
<form actions='simple_edit.cgi' method='POST'>
<textarea rows='10' cols='20' name='text'>%s</textarea><br/>
<input type = 'submit'/>
</form>		

</body>


</html>

"""%text