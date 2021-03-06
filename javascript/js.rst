.. _js:

***************
js
***************

技巧
=============================

checkbox半选状态::

  indeterminate = true;

element.attributes会返回所有属性的数组，每个属性都是一个key为name，value的object

location.replace设置当前文档，并在history中移除，防止后退::

  location.replace('about:blank') 空白页
  location.replace('javascript:""') url不变，页面空白

checkbox使用鼠标选中时，在标签中不会添加checked属性，因此[checked]选择是无效的，可以直接使用node.checked来判断是否选中

is-disabled时禁止点击事件::

  $(function() {
    $('#toggle').click(function() {
      if ($('.btn').hasClass('is-disabled')) {
        $('.btn').removeClass('is-disabled');
      } else {
        $('.btn').addClass('is-disabled');
      }
    });
    $('.btn').click(function(e) {
      if ($(this).hasClass('is-disabled')) {
        e.stopImmediatePropagation();
      }
    });
    $('.btn').click(function() {
      console.log('some');
    });
  });

window.undefined可能会被覆盖，所以void 0才是真正的undefined，而且字符更少

使用concat来实现shallow flatten::

  Array.prototype.concat.apply(Array.prototype,[[2,5],3]) //[2,5,3]

var ctor = function(){};
ctor为constructor构造函数的缩写

IE中无法解析
Date.parse('2013-3-28 15:05:38')

必须为
Date.parse('2013/3/28 15:05:38')

对象为引用赋值，原对象改变新对象也跟着改变，但是如果原对象重新赋值，新对象不变::

  var a = {
    name: 'tom'
  };
  var b = a;
  console.log(b.name); //tom

  a.name = 'jerry';
  console.log(b.name); //jerry

  a = null;
  console.log(b.name); //jerry

document.activeElement用来管理DOM焦点，获得DOM中当前获得焦点的元素。
元素获得焦点的方式有页面加载、用户输入（通常是通过按Tab键）和在代码中调用focus()方法

继承
--------

::

  function Animal() {}
  function Dog() {}

Chrome下::

  // 要让 Dog 继承 Animal, 只需：
  Dog.prototype.__proto__ = Animal.prototype;

  // 实例化后
  var dog = new Dog();
  // dog.__proto__ 指向 Dog.prototype
  // dog.__proto__.__proto__ 指向 Animal.prototype
  // 原型链已成功建立起来，而且很清晰

IE下只能::

  Dog.prototype=new Animate;

Arale做法::

  function Ctor() { }

  // See: http://jsperf.com/object-create-vs-new-ctor
  var createProto = Object.__proto__ ?
    function(proto) {
      return { __proto__: proto }
    } :
    function(proto) {
      Ctor.prototype = proto
      return new Ctor()
    }

  Dog.prototype=createProto(Animate.prototype);


下面的a赋值会将a声明提前，但是赋值没有提前，因此undefined++会输出NaN.
function a(){}与var a=function(){}不同，没有重新给a赋值::

  function fn() {
    return a++;
  }

  function fn2() {
    var a = 1;
    return fn();
  }
  //NaN
  console.log(fn2());

  var a = 3;
  //number
  console.log(typeof a);

  function a() {
    console.log('d');
  }
  //number
  console.log(typeof a);

onclick事件中，如果return false会阻止默认事件发生::

    eleBtn.onclick = function() {
      return false;
    };

变量声明会自动提前到作用域的顶部，但是赋值不会提前::

  if (!("a" in window)) {
      var a = 1;
  }
  alert(a);

相当于::

  var a;
  if (!("a" in window)) {
      a = 1;
  }
  alert(a);

因此答案为undefined


函数声明::

  function functionName(arg1, arg2){
      //函数体
  }

函数表达式::

 b = function a(x) {}

函数声明会提前，函数表达式相当于变量赋值，没有新的声明。

函数声明会覆盖变量声明，但不会覆盖变量赋值::

  function value(){
      return 1;
  }
  var value;
  alert(typeof value);    //"function"

赋值后::

  function value(){
      return 1;
  }
  var value = 1;
  alert(typeof value);    //"number"

arguments会更改传入参数::

  function b(x, y, a) {
      arguments[2] = 10;
      alert(a);              //10
  }
  b(1, 2, 3);

如果第一个参数传入的对象调用者是null或者undefined，call方法将把全局对象（也就是window）作为this的值::

  function a() {
      alert(this);     //[object window]
  }
  a.call(null);

case语句如果不使用break，会继续执行下面的case语句，而不再判断条件::

  switch ('y') {
    case 'y':
      console.log('y');
    case 'other':
      console.log('other');
  }

  结果为:
  y
  other

获取某位置处的元素::

  document.elementFromPoint

document.createDocumentFragment();可以避免每次进行Dom操作时的页面刷新

设置css::

.style.cssText

[2,3].toString() == '2,3'

console.dir()可以显示类.如使用log显示function会返回函数定义内容,而使用dir可以查看整个类结构.

* 2进制转化为10进制：parseInt(a,2)
* 10进制转化为16进制：a.toString(16));

ascii码为10进制

* 字符转ascii码：'a'.charCodeAt() == 97
* ascii码砖字符：String.fromCharCode(65) == 'A'

::

  $('pre').innerHTML
  .replace(/_/g,1)
  .split(/\s/)
  .map(function(i){
    return String.fromCharCode(parseInt(i,2));
  }).join('');

判断为list，而不是object::

  if (obj.length === +obj.length) {}

* object.length  undefined
* +obj.length  NaN

undefined == null

[]会被认为是true::

  > lst = [];
  > if (lst) console.log(true);
  true

在判断中赋值::

  //else false
  if (a=false){
    console.log(a);
  }
  else {
    console.log('else',a);
  }

for (var key in dict)

::

  lst = ['a','b','c']
  2 in lst  //true

lst.length=8  会扩展array长度，不足的为undefined

l.length=0  清空array

有length和序号，可以当作Array来使用::

  var my_object = {
      '0': 'zero',
      '1': 'one',
      '2': 'two',
      '3': 'three',
      '4': 'four',
      length: 5
  };
  var sliced = Array.prototype.slice.call(my_object, 3);

  console.log(sliced);

arg.length说明可以$.each

sort默认按照字符编码对数组进行排序::

  [2,10].sort() //[10,2]

按数字比较::

  [2,10].sort(function(a,b){a-b}) //[2,10]

获取元素宽度，高度::

  $element[0].offsetWidth
  $element[0].offsetHeight

IE中array没有indexOf方法，数组中查找元素::

  String.prototype.indexOf.call(['a','b'],'a')

如果html不规范（比如标签未关闭），那么在IE中赋值给$.html时会静静的失败


chrome中的滑动条控件::

  <input id="rangeCrossFade" type="range" value="50" min="0" max="100" step="10" />


css选择::

  var $ = function(selector) {
      return document.querySelector(selector);
  };

forEach::

  ["-webkit-", "-moz-", "-ms-", "-o-", ""].forEach(function(prefix) {

修改内容::

  eleOpacityImage.innerHTML = '<'

修改css::

  eleImages[1].style.opacity = value / 100;

* 浏览器内部宽度 window.innerWidth
* 整个浏览器的宽度 window.outerWidth
* 显示器宽度 screen.width

解析url
---------------------------

.. image:: location.png

document.documentMode
---------------------------

* 5  Internet Explorer 5 mode (also known as "quirks mode").
* 7  Internet Explorer 7 Standards mode.
* 8  Internet Explorer 8 Standards mode.
* 9  Internet Explorer 9 Standards mode.
* 10  Internet Explorer 10 Standards mode.

json标准格式
---------------

key加双引号

value加双引号，可以为数字（不加引号），可以为list([])

位运算
---------------

http://www.w3school.com.cn/js/pro_js_operators_bitwise.asp

::

  << 左移
  >> 右移
  ~ 非
  & 与
  | 或
  ^ 异或

所有整数字面量都默认存储为有符号整数。只有 ECMAScript 的位运算符才能创建无符号整数。

开发者不能直接访问第 32 个数位，即有符号整数的符号位（在最前面）

无符号整数的数值范围为 0 到 4294967295

32位最多存储整数42亿

::

  var iNum = 18;
  alert(iNum.toString(2));  //输出 "10010"

位运算 NOT 实质上是对数字求负，然后减 1，因此 25 变 -26

escape
-----------

* escape()  已经被废弃，不要使用
* encodeURI()  url编码，编码后仍然可以使用
* encodeURIComponent()  作为url参数编码使用

原来::

  http://www.google.com/a file with spaces.html

encodeURI::

  http://www.google.com/a%20file%20with%20spaces.html

encodeURIComponent::

  http%3A%2F%2Fwww.google.com%2Fa%20file%20with%20spaces.html

参数编码应用::

  param1 = encodeURIComponent("http://xyz.com/?a=12&b=55")
  url = "http://domain.com/?param1=" + param1 + "&param2=99";

结果为::

  http://www.domain.com/?param1=http%3A%2F%2Fxyz.com%2F%Ffa%3D12%26b%3D55&param2=99

通过iframe实现跨域通信
----------------------

http://blog.leezhong.com/tech/2011/01/25/iframe-crossdomain.html

主页面中获取iframe中的元素::

  $(frames['bar'].document).find('#someid')

iframe中获取其他iframe中的元素::

  $(parent.frames['foo'].document).find('#someid')

通过改变隐藏iframe的size来通知发生了某事件，信息通过url hashtag或者页面元素赋值来传递

隐藏iframe::

  <iframe src="http://demo.leezhong.com/crossdomain/proxy.html" name="proxy" id="proxy" style="position:absolute; top:-10px; width:1px; height:1px"></iframe>

改变size::

  $proxy.css('width', $proxy.width()+1+'px');

监听resize事件::

  $(window).resize(function(){});

constructor
-------------------

对象的constructor属性始终指向创建当前对象的构造函数

每个函数都有一个默认的属性prototype，而这个prototype的constructor默认指向这个函数

::

  var Foo=function(){}
  var f = new Foo();

  console.log(f.constructor === Foo); // true
  console.log(Foo.prototype.constructor === Foo);// true
  //合并起来
  console.log(f.constructor.prototype.constructor===Foo);// true

但如果覆盖了prototype::

  Foo.prototype = {
    getName: function() {
      return "name";
    }
  };

此时Person.prototype.constructor === Object

应采用重新覆盖的方式更改::

  Person.prototype.constructor = Person;

播放声音
--------------

chrome中优先使用audio，使用ogg格式文件::

  voice.self = Ext.DomHelper.append(document.body, {tag: 'audio', src: 'horse.ogg'});
  voice.self.play();

如果要使用wav格式::

  IE下{tag: 'bgsound', src: file, loop: 1, autostart: true}
  非IE{tag: 'embed', src: file, hidden: true, autostart: true, loop: false}

图形
=============

开源库

* raphael	svg/vml 绘图
* d3		数据绑定
* datav	数据可视化

方案

* svg在Android 3.0以上版本才支持
* paper.js  canvas绘图

桌面平台使用raphael，移动端使用paper

思考
=============================

javascript三大主神

* Brendan Eich：javascript之父
* Dean Edwards：IE7.js、Base2框架、packer压缩器、cssQuery、moz-behaviors.xml的作者
* Douglas Crockford：JSON、JSLint、JSMin、ADSafe与蝴蝶书的作者


搞清组件的核心功能，果断调用。如jQuery为DOM/Ajax/Anim 操作类库

对于非核心功能，可以考虑在自己组件里实现。如$.extend 或 $.each

IE6/7不支持JSON，需要借助json2.js，其他版本原生支持


js库
=============================

DD_belatedPNG解决IE6下PNG不透明问题

多选控件，包括自动补全，ajax等功能
http://textextjs.com/

类似iphone的手指滑动，滚动屏幕效果
http://natrixnatrix89.github.com/promptu-menu/

moment进行日期解析::

    var moment = require('moment');
    moment().format('YYYY-MM-DD HH:mm:ss')

http://modernizr.com/
检测浏览器对html5和css3的支持情况的库

phantomjs提供headless的浏览器调用，可以模拟浏览器进行操作。

QUnit
----------

A JavaScript Unit Testing framework.

stop(),start()提供了Asynchronous Test，如果不使用的话，异步操作中的断言会无法执行

测试接口是否提供，返回结果是否正确，行为是否符合预期

async
----------

将多层嵌套变为一层，还是需要callback

Jscex
---------

series::

  $await(op1());
  $await(op2());
  $await(op3());

parallel::

  var resultArray = $await(whenAll(op1(), op2(), op3()));

$await等待的是一个异步对象, 待该Task对象结束（返回结果或抛出错误）；如果它尚未启动，则启动该任务；如果已经完成，则立即返回结果（或抛出错误）

在一般编程场景中，如果盲目使用await取代传统的callback，会带来不必要的封装，导致语句理解难度加大。如sample/weibo.html

spm
---------

建立spm目录结构::

  mkdir svg-personnel
  cd svg-personnel/
  spm init

获取模块::

  mkdir libs
  cd libs/
  spm install all

js文件名中不能有“.”，应该使用“-”

js变量名中不能有“-”，改为驼峰式

require('./jquery.mousewheel')会导致spm build时认为要寻找jquery.js，因此改为require('./jquery-mousewheel')

如果不build到modules中，那么类中的this指向window

去掉coffee打包::

  spm build --enableCoffee=false

bootstrap
-----------

<button>会有默认的点击事件，会导致页面重新加载，因此使用<a>来代替

bootstrap-transition.js返回css transition的函数名，例如chrome下为{end: "webkitTransitionEnd"}
通过调用css transition在现代浏览器中实现动画效果

bootstrap-dropdown.js通过toggleClass('open')实现下拉列表的显示和隐藏

underscore
--------------

生成_的新对象，将obj保存在this._wrapped中，以便通过value方法取得最终值。

chain方法标记_chain为true，以供内部函数result返回新的_对象来进行链式调用

_.bind模拟Function.bind(), 不仅能将函数绑定为方法，而且可以作为柯里化使用
