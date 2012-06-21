.. _linux:


***************
linux
***************

目前两大主流linux桌面系统GNOME/GTK和 KDE/Qt

基本操作
=============================

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

工具
=============================

代码统计: `cloc <http://cloc.sourceforge.net/>`_

fedora启动失败
=============================

启动fedora，提示::

	Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)

更换其他内核可以进入

查看/bin/grub2/grub.cfg, 发现最新内核下少了initrd/boot/initramfs-\*.img

重新生成img::

	$ yum reinstall kernel

下载整个网站
=============================

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

SELinux
=============================

SELinux 全称 Security Enhanced Linux (安全强化 Linux)，是 MAC (Mandatory Access Control，强制访问控制系统)的一个实现，目的在于明确的指明某个进程可以访问哪些资源(文件、网络端口等)。
http://linuxtoy.org/archives/selinux-introduction.html
http://www.linux.gov.cn/netweb/selinux.htm

获取当前 SELinux 运行状态::

	$ getenforce

暂时改变 SELinux 运行状态::

	$ setenforce 0

看看到底是不是 SELinux 导致某个服务或者程序无法运行

配置php环境
=============================

::

	yum install php

在/var/www/html中创建测试文件info.php::
 
	<?php 
		phpinfo(); 
	?>

可以看到测试页面。

::

	yum install php-mysql php-gd php-imap php-ldap php-odbc php-pear php-xml php-xmlrpc php-eaccelerator php-magickwand php-magpierss php-mapserver php-mbstring php-mcrypt php-mhash php-mssql php-shout php-snmp php-soap php-tidy

重启Apache2::

	$ service httpd restart


Fedora 10里将普通用户添加到sudo组
=======================================

1. 在终端输入su -
#. 输入密码， 这样就切换到root了
#. 输入visudo
#. 找到 root ALL=(ALL) ALL 在这一行下边按a键进入编辑模式，然后输入： yourname ALL=(ALL) ALL,然后按esc退出
#. 按 :wq 键保存退出
#. 输入exit退出root权限
#. 测试，在当前用户下，输入sudo whoami

如果一切正常，命令会返回 “root” 这个字。
