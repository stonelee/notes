.. _node:

***************
node
***************

package.json中dependencies格式::

  "~1.2.3" = ">=1.2.3 <1.3.0"

生产环境下 npm install --production 将不安装devDependencies中的包

* module.exports定义的函数可以require后直接调用
* exports定义的函数无法调用，只能引用

对于有package.json的node项目，使用npm安装其依赖，-g使得命令行可以调用bin目录中的程序::

	# npm install -g

会安装到::

    /usr/local/lib/node_modules

npm install -g会安装为命令行工具，但是node环境下依然无法require该类库，会报错::

  Error: Cannot find module 'uglify-js'

需要在安装到本目录的node-modules中::

  $ npm install uglify-js

查看安装细节，找到问题::

	npm install --verbose

对于安装失败的包,手工下载tgz文件,然后::

	npm install some.tgz --verbose

控制台彩色字体::

  node -e 'process.stdout.write("\033[32m\033[1mhello world\033[0m")'

socketio
==========

安装redis::

    make
    yum install tcl

写密集型操作放到redis中

基于Multi-process and multi-machine scaling考虑，使用redis pub-sub来扩展socket.io，而且这样还可以供其他redis客户端使用。

::

    var socketio = require("socket.io")
    var redis = require("redis")

    // redis clients
    var store = redis.createClient()
    var pub = redis.createClient()
    var sub = redis.createClient()

    // ... application paths go here

    var socket = socketio.listen(app)

    sub.subscribe("chat")

    socket.on("connection", function(client){
      client.send("welcome!")

      client.on("message", function(text){
        store.incr("messageNextId", function(e, id){
          store.hmset("messages:" + id, { uid: client.sessionId, text: text }, function(e, r){
            pub.publish("chat", "messages:" + id)
          })
        })
      })

      client.on("disconnect", function(){
        client.broadcast(client.sessionId + " disconnected")
      })

      sub.on("message", function(pattern, key){
        store.hgetall(key, function(e, obj){
          client.send(obj.uid + ": " + obj.text)
        })
      })

    })

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

grunt
============

grunt的async提供了promise机制::

  // Tell grunt this task is asynchronous.
  var done = this.async();

  // Write the contents of the target file to the new location
  fs.writeFile(pathToWrite, data, function (err) {
    if (err) throw err;
    console.log(pathToWrite + ' saved!');
    // Tell grunt the async task is complete
    done();
  });

  http.get(pathToRead, function(res) {
    // Pipe the data from the response stream to a static file.
    res.pipe(fs.createWriteStream(pathToWrite));
    // Tell grunt the async task is complete
    res.on('end', function() {
      console.log(pathToWrite + ' saved!');
      done();
    });
  }).on('error', function(e) {
    console.log("Got error: " + e.message);
    // Tell grunt the async task failed
    done(false);
  });

使用chrome调试node程序node-inspector
=========================================

Install::

  $ npm install -g node-inspector

启动被调试的程序::

  $ node --debug-brk your/short/node/script.js

打开调试后端::

  $ node-inspector &

在chrome中打开页面 http://127.0.0.1:8080/debug?port=5858 ，可以下断点，各种调试

常用库
==========

jinja(Swig): django模板

jshint: 代码静态检查

mocha: js test framework

should: node中使用，扩展了Object

robotskirt: markdown解析

各种node资源
================

http://nodeknockout.com/resources
