.. _node:

***************
node
***************

对于有package.json的node项目，使用npm安装其依赖，-g使得命令行可以调用bin目录中的程序::

	# npm install -g

查看安装细节，找到问题::

	npm install --verbose

对于安装失败的包,手工下载tgz文件,然后::

	npm install some.tgz --verbose

express
============

安装：$ sudo npm install -g express

源码安装::

	git clone https://github.com/visionmedia/express.git 
	git submodule update --init 
	make install 
	make install-support 

建立project::

	$ express /tmp/foo
	$ cd /tmp/foo/
	安装依赖：
	$ npm install -d
	（-d 可视化形式显示）

启动::

	$ node app.js

curl http://localhost:3000/users/1

::

	var app = require('express').createServer();

	app.get('/', function(req, res){
	  res.send('hello world');
	});

	app.listen(3000);

connect
============

logger记录日志，可控制格式

bodyParser根据content-type解析提交的内容，其中数据放在req.body，文件放在req.files

目前支持：

* application/json
* application/x-www-form-urlencoded
* multipart/form-data

methodOverride在req.method中存放method，用来rest，原来的method放在req.originalMethod中。form中使用_method来提交rest method

cookieParser将cookie放到req.cookies中

session提供了基于memory等的session操作，通过req.session访问
