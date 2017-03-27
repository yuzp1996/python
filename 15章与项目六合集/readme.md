## 血的教训

在cgi-bin文件下只能放置cgi脚本，要是放置html模板的话，拿就要换一个文件夹了，要不总是提示错误

    [Mon Mar 27 20:34:03.731653 2017] [cgi:error] [pid 1410:tid 140352375736064] [client ::1:41224] AH01215: (8)Exec format error: exec of '/var/www/cgi-bin/html/index.html' failed: /var/www/cgi-bin/html/index.html
[Mon Mar 27 20:34:03.731867 2017] [cgi:error] [pid 1410:tid 140352375736064] [client ::1:41224] End of script output before headers: index.html


妈的，恶心死了，这个文件要放到与cgi-bin同级的html文件夹中，这个文件下才能引用html文件，妈的，老子被坑死了。

访问的话

http://localhost/index.html

直接加上文件名即可
