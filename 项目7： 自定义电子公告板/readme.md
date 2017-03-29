如何将mysql提出的数据作为字典形式

http://www.jb51.net/article/54166.htm

因为我用的是mysql数据库，所以接入的方式和书上的不一样，因为没有dicfetchall()方法，所以用的是

    import MySQLdb.cursors
conn = MySQLdb.connect(host="localhost",user="root",passwd="admin", db="test",cursorclass = MySQLdb.cursors.DictCursor)

这个方式，这个东西一直都是要授权，要不在error.log中是看不到错误提示的，

访问的时候要这样

http://localhost/cgi-bin/project7/main.cgi

因为我是在cgi-bin文件夹下的，所以要这样子来访问
