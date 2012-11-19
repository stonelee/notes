.. _jquery:

***************
jquery
***************

$.ajax()返回jqXHR，是XMLHTTPRequest的超集

判断是否找到::

	$('#id').length ? 'exist' : 'not'

jquery1.7.2中如果在setInterval中循环getJSON同一个地址时，chrome不会显示发送xhr请求，但是firefox中会显示。jquery1.4.2没有这个问题

$.extend可以merge objects，第一个参数true递归merge(deep copy for object and array)

防止修改defaults参数::

	var settings = $.extend({}, defaults, options);

jquery中.data('kjGrid')，调用时使用kjGrid，kj-grid都可以。反之亦然

只序列化有name的input，select，textarea；check，radio如果没选中不加入序列，选中会返回on

intro，outro提供包裹函数，其他函数可以作为全局函数测试，生产环境时打包到一起

jQuery.fn中的this是个[]

* event.stopImmediatePropagation()	阻止冒泡，也阻止其他handlers
* event.stopPropagation() 	阻止冒泡

event设置命名空间name，方便统一处理同类型的事件::

	bind('click.name',handler)
	unbind('.name')

offsetParent()得到positioned的最近的父元素(relative,absolute,fixed)

event.pageX,pageY得到相对于document左上角的鼠标位置坐标

* offset得到相对document的第一个元素的坐标
* position得到相对于offset parent的坐标

clone可以复制选择的element，第一个参数为true可以连同event和data一起复制，第二个参数为true可以连同children一起复制，注意不要复制有id的，这样会导致id重复。对于data中的objects和arrays依然需要$.extend([],$elem.data('arr'))才能做到深复制

高亮某项，去掉其他项的高亮::

	if ( !$event_counter.hasClass( "ui-state-hover" ) ) {
		$event_counter.addClass( "ui-state-hover" )
			.siblings().removeClass( "ui-state-hover" );
	}

限制查找范围,第二个参数为上下文，可以代替find::

	$( "span.count", $event_counter ).text( new_count );

text获取所有文本，去除html标签，可应用于xml和html，对于input或者textarea使用val，对于script使用html。text()赋值时会将html标签转义。

typeof null == 'object'
所以要使用$.isPlainObject()来判断是不是object

判断::

	empty string is falsey, 
	empty array with .length == 0
	empty objects	with $.isEmptyObject()

$.getScript()加载js文件并执行，不缓存

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

jquery UI
====================

::

	$.widget('custom.colorize',{options:{}})

定义了custome命名空间下的colorize控件。
options为配置参数，使用this.options.name来调用。还包括回调函数，使用this._trigger('')来调用。用户实例化控件时直接定义即可。
this.element为调用该控件的jquery对象。

不以下划线开头的函数为公开函数，可以通过.colorize('hello')来调用。

实例化方法::

	$("#myid").colorize({});

引用所有实例::

	$(':custom-colorize')


寻找data中有droppable的::

	this.element.find(":data(droppable)")

jqueryui中widget中通过this定义函数和变量会保存在$('#id').data()中

draggable的scroll针对父元素overflow:auto有效，这时scrollParent不为document；如果使用body的滚动条会出现元素消失的现象

data中保存类信息

添加selector::

  jQuery.expr[':'].inline = function(elem) {
      return jQuery(elem).css('display') === 'inline';
  };

调用::

  jQuery('div a:inline').css('color', 'red');

$.widget.extend 对于{}类型的对象进行深复制，貌似相当于$.extend(true,{},...)

$.widget.bridge将一般的对象桥接到jquery上，自动创建实例并存储在元素的data中，实例化后允许调用公共方法，不允许调用私有或者不存在的方法，防止多次实例化。
约定该对象参数为options,element，_init()为初始方法，option为配置参数方法。

