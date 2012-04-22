.. _mysql:


***************
mysql
***************

安装
=============================

安装::

	sudo apt-get install mysql-server

一旦安装完成，MySQL 服务器应该自动启动::

	sudo start mysql #手动的话这样启动
	sudo stop mysql #手动停止

检查 mysqld 进程是否已经开启::

	pgrep mysqld //返回该进程的id

重启::

	/etc/init.d/mysql restart

基本命令
=============================

登录::

	mysql -u root -p

查看有哪些数据库::

	show databases;

使用某数据库::

	use ciis;

查看有哪些表::

	show tables;

查看mysql环境变量::

	show variables;

查看版本::

	/etc/init.d/mysql --version

删除数据库::

	drop database ciis;

导入sql数据::

	source ~/Develop/node/coffee-mvc/file_client/db_create.sql

编码问题
=============================

查看字符变量:: 

	show variables like '%char%';

暂时修改字符集::

	set character_set_database=utf8; 

防止字符乱码，永久修改字符集

在个人目录下建立mysql配置文件::

	$cp /etc/mysql/my.cnf ~/.my.cnf

修改.my.cnf::

	[client]
	default-character-set=utf8

	[mysqld]
	default-character-set = utf8
	skip-character-set-client-handshake
	character-set-server = utf8
	collation-server = utf8_general_ci
	init-connect = SET NAMES utf8
