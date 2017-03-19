## 使用说明以及拓展需求


这是基于python socket做的聊天室，具体的用法如下
****
##### 这几个都是服务器，由简单到复杂，开启的方法很简单，用命令行方式的话
 
> python chatserver.py

即可开启服务
****
客户端运行telnet服务，
> telnet localhost 5005

**端口默认5005**

****
进入后的命令只有 
>login <name>

>logout

>who

>say <message>

>look

### 快来试试或者来拓展它吧
***
### 现在已经做了一些拓展，命令也增加了一些

管理员踢人 只有用admin登入才可以实现踢人
> getout

> say 命令已经没有了，login 后可以直接输入你想说的话