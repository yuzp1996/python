#!/usr/bin/python

print 'Content-type:text/html\n'
print
import cgitb;cgitb.enable()
import MySQLdb
import MySQLdb.cursors
conn = MySQLdb.connect(host="localhost",user="root",passwd="admin", db="test",cursorclass = MySQLdb.cursors.DictCursor)

curs = conn.cursor()

print '''
<html>
  <head>
    <title>The UserNet</title>
  </head>
  <body>
    <h1>The UserNet</h1>
'''

sql = 'SELECT * FROM messages'
curs.execute(sql)

rows = curs.fetchall()
toplevel = []
children = {}

for row in rows:
        parent_id = row['reply_to']
        if parent_id is None:
                toplevel.append(row)
        else:
                children.setdefault(parent_id,[]).append(row)

        def format(row):
                print '<p><a href="view.cgi?id=%(id)i">%(subject)s<a></p>' % row
                try:
                        kids = children[row[0]]
                except KeyError:
                        pass
                else:
                        print '<blockquote>'
                        for kid in kids:
                                format(kid)

                        print '</blockquote>'

        print '<p>'

        for row in toplevel:
                format(row)

print '''
</p>
<hr/>
<p><a href="edit.cgi">Post Message</a></p>
</body>
</html>
'''
