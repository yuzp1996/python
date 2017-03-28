## 血的教训

在cgi-bin文件下只能放置cgi脚本，要是放置html模板的话，拿就要换一个文件夹了，要不总是提示错误

    [Mon Mar 27 20:34:03.731653 2017] [cgi:error] [pid 1410:tid 140352375736064] [client ::1:41224] AH01215: (8)Exec format error: exec of '/var/www/cgi-bin/html/index.html' failed: /var/www/cgi-bin/html/index.html
[Mon Mar 27 20:34:03.731867 2017] [cgi:error] [pid 1410:tid 140352375736064] [client ::1:41224] End of script output before headers: index.html


妈的，恶心死了，这个文件要放到与cgi-bin同级的html文件夹中，这个文件下才能引用html文件，妈的，老子被坑死了。

访问的话

http://localhost/index.html

直接加上文件名即可

###  一定要对text或者html文件进行授权  

问题查不出来很棘手

    try:
        f = open(join(BASE_DIR, filename), 'w')
    except Exception as err:
        print err  
        print "1"


还是靠这个把问题揪出来了

Errno 13] Permission denied: '/var/www/cgi-bin/data/first' 1 

出了一大推的错，感觉自己也是恶心坏了，授权的问题也解决了，要是需要写的文件授权就要给666这个权限，这个恶心死我了，昨晚一晚上，这家伙，

 sudo chmod 666 first

对于修改cgi程序的权限。CGI程序属性一定要设为可运行（755），而与CGI有关的HTML文件的目录如果要被CGI程序写入，其权限一定要设为可写（666）
