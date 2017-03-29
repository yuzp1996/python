#!/usr/bin/python
print 'Content-type: text/html\n'
import cgitb; cgitb.enable()
import MySQLdb.cursors

import MySQLdb
conn = MySQLdb.connect(host="localhost",user="root",passwd="admin", db="test",cursorclass = MySQLdb.cursors.DictCursor)
curs = conn.cursor()

def format(row):
    print row['subject']
    try: kids = childern[row['id']] 
    except KeyError: pass
    else:
         print '<blockquote>'
         for kid in kids:
            format(kid)
         print '</blockquote>'


print """
   <html>
<head>
<title>The Foobar Bulletin Board</title>
</head>
<body>
<h1>the  Foobar Bulletion Board</h1>
"""
curs.execute('SELECT * FROM messages')
rows = curs.fetchall()


toplevel = []
childern = {}
print rows
for row in rows:
   
    parent_id = row['reply_to']
    if parent_id is None:
        toplevel.append(row)
    else:
        childern.setdefault(parent_id,[]).append(row)

    print '<p>'

    for row in toplevel:
       format(row)

print """
</p>
</body>
</html>
"""















