.. _jquery:

***************
jquery
***************

jquery1.7.2中如果在setInterval中循环getJSON同一个地址时，chrome不会显示发送xhr请求，但是firefox中会显示。jquery1.4.2没有这个问题

$.extend可以merge objects，第一个参数True递归merge

防止修改defaults参数::

	var settings = $.extend({}, defaults, options);


jquery中.data(‘kjGrid’)，调用时使用kjGrid，kj-grid都可以。反之亦然

只序列化有name的input，select，textarea；check，radio如果没选中不加入序列，选中会返回on

intro，outro提供包裹函数，其他函数可以作为全局函数测试，生产环境时打包到一起

jQuery.fn中的this是个[]

Callbacks
====================

$.Callbacks()可以将一组函数进行统一调用。

可以使用add，remove来操作，通过fire来调用

* once	只能执行一次fire
* momory	对于fire后面的add语句，仍然使用原值进行fire，就好像先add再fire一样，对remove无效
* unique	如果多次add同一个函数，list中只保留一次
* stopOnFalse	list中的函数如果返回false则不继续执行

$.Callbacks()返回object，包含add，remove等函数，这几个函数又return this，可以保证链式操作

Callbacks实现pub/sub解耦，以及使用deferred进一步解耦::

	function fn1(value) {
		console.log(value);
		return 'result'
	}

	function fn2(value) {
		fn1("fn2 says:" + value);
		return false;
	}

	var topics = {};

	jQuery.Topic = function(id) {
		var callbacks, method, topic = id && topics[id];
		if (!topic) {
			callbacks = jQuery.Callbacks();
			topic = {
				publish: callbacks.fire,
				subscribe: callbacks.add,
				unsubscribe: callbacks.remove
			};
			if (id) {
				topics[id] = topic;
			}
		}
		return topic;
	};

	$.Topic("mailArrived").subscribe(fn1);

	//pub/sub
	$.Topic( "mailArrived" ).publish( "hello world!" );

	//deferred
	var topic = $.Topic("mailArrived");

	var dfd = $.Deferred();
	dfd.done(topic.publish);

	dfd.resolve("its been published!");

Deferred
====================

http://www.ruanyifeng.com/blog/2011/08/a_detailed_explanation_of_jquery_deferred_object.html

Deferred可以用来屏蔽异步/同步操作的差异::

	var cache = {};

	function getData( val ){

		// return either the cached value or an
		// jqXHR object (which contains a promise)
		return cache[ val ] || $.ajax('/foo/', {
			data: { value: val },
			dataType: 'json',
			success: function( resp ){
				cache[ val ] = resp;
			}
		});
	}

	$.when(getData('foo')).then(function(resp){
		// do something with the response, which may
		// or may not have been retreived using an
		// XHR request.
	});

方便多个操作::

	$.when( $.getJSON('/some/data/'), $.get('template.tpl') ).then(function( data, tmpl ){

		$( tmpl ) // create a jQuery object out of the template
			.tmpl( data) // compile it
			.appendTo( "#target" ); // insert it into the DOM

	});

编译jquery
================

node切换到正式版本::

	$ git checkout v0.6.19-release

编译::

	# ./configure
	# make
	# make install
 
查看node版本::

	$ node --version
	v0.6.19

进入jquery目录，安装node依赖::

	$ cd jquery && npm install

编译jquery::

	$ node_modules/grunt/bin/grunt
