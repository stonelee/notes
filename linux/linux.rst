.. _linux:


***************
linux
***************

目前两大主流linux桌面系统GNOME/GTK和 KDE/Qt

基本操作
=============================

::

	echo '$var'	#原样输出
	echo “$var”	#解释后输出

	printf	格式化输出

文件夹中查找字符串::

	$ grep 'makeprg' * -r

指定文件中查找字符::

	grep text filename.js

搜索文件名::

	$ find . | grep '开发'

或者::

	find '/home' -name "abc*.conf"

从某扩展名中搜索::

	$ find . -name "*.xx" | xargs grep -r "key"

定位命令::

	$ which [ 

树状形式显示当前文件夹下的两层目录结构::

	tree -L 2 .

查看系统资源使用情况：top （P 按CPU排序；M 按内存使用排序）

ssh::

	ssh vboxadmin@10.10.22.86

查看端口号被谁占用::

	lsof -i:80


级联更改文件夹权限::

	chmod -R 777 dir/

随机启动::

	sudo chkconfig --levels 235 mongod on

图形界面打开当前文件夹::

	$ gnome-open .

安装源里没有的程序::

	在http://pkgs.org/下载相应的rpm文件，然后
	rpm -ivh PIL-1.1.7-10.fc16.i686.rpm 

下载远程文件::

	$ scp -r vboxadmin@10.10.22.86:/home/vboxadmin/Videos/冰冻星球/ /media/程序

查看进程::

	ps -aux |grep mongo

查看安装的软件::

	rpm -qa | grep kernel

查看内核::

	uname -r

查看所有内核信息::

	uname -a

ssh
-----------------

ssh scp sftp访问远程机器免输入密码

本机生成密钥::

  $ ssh-keygen -t rsa

公共密钥保存在 ~/.ssh/id_rsa.pub
私有密钥保存在 ~/.ssh/id_rsa

将公共密钥复制到要访问的机器上::

  $ scp ~/.ssh/id_rsa.pub vboxadmin@10.10.22.86:/home/vboxadmin/.ssh/authorized_keys

工具
-----------------

代码统计: `cloc <http://cloc.sourceforge.net/>`_

下载整个网站
-----------------

::

	$ wget -U "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB5)" -r -p -k -nc -np -o down.log https://www.django-cms.org/ --no-check-certificate

===	===
-U	修改agent
-r	递归
-nc	不下载已经存在的文件
-np	表示不跟随链接，只下载指定目录及子目录里的东西；
-p	下载页面显示所需的所有文件。比如页面中包含了图片，但是图片并不在/yourdir目录中，而在/images目录下，有此参数，图片依然会被正常下载。
-k	修复下载文件中的绝对连接为相对连接，这样方便本地阅读。
===	===

--no-check-certificate	https链接需要


curl
-----------------

crud貌似有问题，使用firefox插件Poster来代替::

	curl -v -H "Content-Type:application/json" -H "Accept:application/json" \
		 -d  "{\"location\":{\"name\":test, \"desc\":\"testdesc\"}}" \
		 http://api.waldstat.com/locations/create?api_key=1234567890abcdefghijk

	-v	显示交互详细信息
	-i	显示response头信息
	-H	附加请求头
	-X	pass a HTTP method name
	-d	添加参数

POST::

	curl -i -H "Accept: application/json" -X POST -d "firstName=james" http://192.168.0.165/persons/person

PUT::

	curl -i -H "Accept: application/json" -X PUT -d "phone=1-800-999-9999" http://192.168.0.165/persons/person/1

GET::

	curl -i -H "Accept: application/json" "http://192.168.0.165/persons?firstName=james&lastName=wallis"

DELETE::

	curl -i -H "Accept: application/json" -X DELETE http://192.168.0.165/persons/person/1


jobs
-----------------

::

	command& 让进程在后台运行，但是关闭终端后程序停止运行
	nohup command& 忽略终端断开，只能用kill关闭, 默认将输出到nohup.out文件中，如果想输入到其他文件中，就用到linux中的输入输出重定向。
	jobs 查看后台运行的进程 
	fg %n 让后台运行的进程n到前台来 
	bg %n 将一个在后台暂停的命令，变成继续执行   

	kill %1
	jobs -l 可显示pid

	ctrl + z 将一个正在前台执行的命令放到后台，并且暂停

输入输出重定向
-----------------

输入输出重定向用符号" <"和">"来表示

0、1和2分别表示标准输入、标准输出和标准错误信息输出

2>a.txt 表示将错误信息输出到文件a.txt中。 

2>&1 表示将错误信息重定向到标准输出

>log 表示把标准输出重新定向到文件log中 

>& log 表示把标准输出和错误输出都定向到文件log中，相当于 >log 2>&1

不需要回显程序的所有信息时，就可以将输出重定向到/dev/null。 

如果想要正常输出和错误信息都不显示，则要把标准输出和标准错误都重定向到/dev/null， 例如： 

# ls 1>/dev/null 2>/dev/null 


基本理论
=============================

SELinux
------------

SELinux 全称 Security Enhanced Linux (安全强化 Linux)，是 MAC (Mandatory Access Control，强制访问控制系统)的一个实现，目的在于明确的指明某个进程可以访问哪些资源(文件、网络端口等)。
http://linuxtoy.org/archives/selinux-introduction.html
http://www.linux.gov.cn/netweb/selinux.htm

获取当前 SELinux 运行状态::

	$ getenforce

暂时改变 SELinux 运行状态::

	$ setenforce 0

看看到底是不是 SELinux 导致某个服务或者程序无法运行

链接
--------------

可以通过软链接来以虚拟路径的方式共享文件：ln -s 源文件夹 目标文件夹

硬链接相当于新建一个文件指针，只有将全部指针删除后，文件内容才会从磁盘上删除。缺点是不可以在不同文件系统的文件间建立链接，不能为目录创建硬链接。

软链接(-s)相当与建立新的快捷方式，没有任何文件系统的限制，可以创建指向目录的符号链接。缺点是如果源文件路径改变，那么链接失效，而且要系统分配额外的空间用于建立新的索引节点和保存原文件的路径。

一般config文件用硬链接即可。引用lib包（如extjs）可使用软链接

Unix目录结构
----------------

《Unix文件系统结构标准》（Filesystem Hierarchy Standard）
http://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard

::

	/：存放系统程序，也就是At&t开发的Unix程序。
	/usr：存放Unix系统商（比如IBM和HP）开发的程序。
	/usr/local：存放用户自己安装的程序。
	/opt：在某些系统，用于存放第三方厂商开发的程序，所以取名为option，意为"选装"。


