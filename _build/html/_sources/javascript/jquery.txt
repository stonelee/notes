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

* event.stopImmediatePropagation()  阻止冒泡，也阻止其他handlers
* event.stopPropagation()   阻止冒泡

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
  empty objects with $.isEmptyObject()

$.getScript()加载js文件并执行，不缓存

$('li.item-ii').find('li') is equivalent to $('li', 'li.item-ii')

.is() is often useful inside callbacks, such as event handlers
positional selectors（如li:first）会在整个document中寻找

插入jquery
==============

::

  var head=document.getElementsByTagName('head')[0]
  var node = document.createElement('script')
  node.src="http://code.jquery.com/jquery.js"
  head.appendChild(node)

注意：http方式获取的js不能插入到https方式获取的页面中

Callbacks
====================

$.Callbacks()可以将一组函数进行统一调用。

可以使用add，remove来操作，通过fire来调用

* once  只能执行一次fire
* momory  对于fire后面的add语句，仍然使用原值进行fire，就好像先add再fire一样，对remove无效
* unique  如果多次add同一个函数，list中只保留一次
* stopOnFalse list中的函数如果返回false则不继续执行

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

CAllbacks（'once memory'）适合做hook，参见_queueHooks

$.Callbacks('memory') 会在add(fn)后使用原值自动fire，使得后来add的方法也被之前fire过的值调用

once使得只fire一次

::

  function fn1(value) {
    console.log('fn1: '+value);
  }

  function fn2(value) {
    console.log('fn2: '+value);
  }

  var callbacks = $.Callbacks("once");
  callbacks.add(fn1);
  callbacks.add(fn2);
  callbacks.fire("bar");
  callbacks.fire("foo");

  //fn1: bar
  //fn2: bar

  var callbacks = $.Callbacks("memory");
  callbacks.add(fn1);
  callbacks.fire("bar");
  callbacks.add(fn2);
  callbacks.fire("foo");

  //fn1: bar
  //fn2: bar
  //fn1: foo
  //fn2: foo

* callbacks.disable() callback完全不再执行
* callbacks.lock() 如果memory，那么原来fire的仍然会执行新的add方法

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

jQuery.get returns a jqXHR object, which is derived from a Deferred object,
动画也是

jQuery.Deferred()构造函数

jQuery.when()包裹deferreds，如果为一般的object，则为resolved状态

.promise( [type ] [, target ] )将jquery对象包装为promise object，主要用于动画中。
默认type为'fx'，意思是动画结束后resolved。
如果有target，将返回包装后的target，而不是新创建一个
保存在.data()中，因此remove方法会将其删掉，如果想在执行后再删掉，应使用detach，等resolve后removeData

::

  $("button").on( "click", function() {
    $("p").append( "Started...");

    $("div").each(function( i ) {
      $( this ).fadeIn().fadeOut( 1000 * (i+1) );
    });

    $( "div" ).promise().done(function() {
      $( "p" ).append( " Finished! " );
    });
  });

deferred.promise()返回promise，只有与改变执行状态无关的方法（如done，fail），没有resolve，reject等方法，从而对deferred对象进行了保护

::

  state:pending, resolved, rejected

  then, always, done, fail, progress
  resolve, resolveWith, reject, rejectWith, notify, notifyWith

deferred.then( doneFilter [, failFilter ] [, progressFilter ] )同时设定多种状态响应

always无论接收与否，done接收，fail拒绝

可以作为filter使用

data
========

jQuery.data()可以安全方便的在dom中存取数据，避免内存泄漏

event handlers等也保存在data中

xml中不能使用，因为IE不支持

animate
===========

show，hide以左上角收缩扩展
slideUp， slideToggle向上收缩，向下扩展

.animate可以使用数字型的css属性进行动画

queue
==========

::

  $("div").queue(function () {
    $(this).addClass("newcolor");
    $(this).dequeue();
  });

queue存储到private_data里

event
=============

即使on('foo.on')也使用elem.addEventListener

::

  jQuery.Event = function( src, props ) {
    // Allow instantiation without the 'new' keyword
    if ( !(this instanceof jQuery.Event) ) {
      return new jQuery.Event( src, props );
    }

jQuery._data( cur, "events" )

remove()会将节点连同里面的节点一起删除，包括data和events。
如果想保留data和event，使用detach()

.addBack()将stack中保存的前面的元素加到当前的集合中

绑定的事件可以查询
jQuery._data(jQuery("#foo")[0], "events");

bind with data, trigger with data::

  var handler = function(event, data) {
      //Object {name: "tom"} "d"
      console.log(event.data,data);
    };

  jQuery("#foo").on("click", {name:'tom'},handler);
  jQuery("#foo").trigger("click",'d');


可以一次绑定多个事件::

  bind("click mouseover", handler)

命名空间::

  bind("focusin.a",f)


自定义事件::

 jQuery.event.special["test"] = {
    _default: function(e, data) {},
    setup: function() {},
    teardown: function() {},
    add: function(handleObj) {},
    remove: function() {}
  };

  bind后触发setup，add
  trigger后触发绑定的事件，_default
  unbind后触发remove，teardown

绑定多个事件::

  .bind({
    "click":handler,
    "mouseover":handler
  },2)

只触发一次::

  .one()

1.7jquery使用on off one代替之前的bind，delegate，live

为方便remove和trigger，可以使用命名空间

event handler如果只是return false那么可以只指定false即可

IE8以下change，sbumit等事件没有冒泡，所以jquery进行了模拟

如果没有指定selector，那么事件在该节点上触发或者冒泡到该节点都会响应。
如果指定了selector，那么只能冒泡才响应.

只能绑定执行on方法时页面中存在的节点，如果要绑定未来的节点，使用冒泡.
可以用于MVC结构的container元素，或者整个document（存在于head，因此可以在其他元素加载完成前获得）

* 阻止附加的其他事件发生，也阻止冒泡event.stopImmediatePropagation()
* 阻止冒泡event.stopPropagation()
* 阻止浏览器默认事件发生event.preventDefault()

return false = event.stopPropagation() + event.preventDefault();

event.target是事件发生的节点，this是事件被附加或者selector的节点，两者可能不一致

object, embed, applet不能附加data，因此不能附加jquery events

focus和blur在W3C标准中不能冒泡，但是jQuery中实现为focusin和focusout可以冒泡？？？

load，scroll, error不能冒泡，IE8以下paste，reset不能冒泡，因此这些事件都不能delegate

window.onerror参数和返回值都不同，因此在jquery中没有支持

expando
===========

expando 是 expandable object 的缩写，表示可扩展的对象。

expando property 表示可扩展对象的动态属性，运行时添加的。expando 可以直接表示 expando property.

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

