.. _performance:

******************
高性能JavaScript
******************

Chapter 2 Data Access
------------------------

越现代的浏览器这些优化越不明显

Literal values和Variables要快于Array items和Object members

作用域链越深，读写越慢。因此如果使用全局变量多于一次，可以使用内部变量进行引用

with可以改变作用域链，会将with指定值的作用域作为第一链，而原来的内部变量成为第二链，反而影响了调用性能

catch也会改变作用域链，因此在catch中的语句越少越好，可以采用如下方法优化::

  try {
      methodThatMightCauseAnError();
  } catch (ex){
      handleError(ex);  //delegate to handler method
  }

with，catch，eval都是dynamic scopes，也就是作用域只能在代码执行过程中确定，而静态分析无法判断，
因此无法在现代浏览器中进行优化，所以要谨慎使用

闭包会创建自己的作用域链，因此会占用更多的内存。
尤其IE中的DOM Objects不是原生Javascript对象，因此在销毁时会导致内存泄露。
而且闭包作为out of scope变量，引用速度不如内部变量快，可以通过内部变量引用的方式解决。

Firefox, Safari, and Chrome可以使用__proto__取得其原型

原型链越长，方法调用越慢

nested调用越长越慢，例如window.location.href

如果方法不存在将更慢

如果在某函数中调用某对象的方法超过一次，最好将其使用内部对象进行引用，但是方法使用this的话除外


CHAPTER 3 DOM Scripting
-----------------------------

DOM scripting is expensive

* IE中的js实现是JScript，位于jscript.dll;DOM实现位于mshtml.dll，内部称为Trident
* Safari使用WebKit’s WebCore实现DOM,js引擎为dubbed SquirrelFish
* Chrome使用WebKit渲染页面，js引擎为V8
* Firefox使用Gecko渲染页面，js引擎为SpiderMonkey

两者的独立使得DOM操作比较慢（通信需要代价）

innerHTML比标准createElement要快一些（IE6中快3倍），但是在webkit中要慢一些。因此更应该从可读性、可维护性方面进行考虑。

使用element.cloneNode()来代替document.createElement()会快一丁点

HTML Collections是类似array的节点数组，
例如document.getElementsByName()，document.getElementsByClassName()，document.getElementsByTagName()，
document.images，document.links，document.forms，document.forms[0].elements（All fields in the first form on the page）.
会在document更新时自动更新，尤其在循环中会有严重的效率问题，因此应在循环外面使用内部变量引用（包括要使用的length）::

  // length导致不停的查询，结果死循环
  var alldivs = document.getElementsByTagName('div');
  for (var i = 0; i < alldivs.length; i++) {
      document.body.appendChild(document.createElement('div'))
  }

在遍历dom的问题上，nextSibling比childNodes方法在IE上要好的多

childNodes, firstChild, nextSibling这样的DOM属性不区分element nodes和其他节点（例如comments，text nodes，空格换行）.
现代浏览器提供了只获取element的属性，IE中只有children，但是IE中的children要远远快于childNodes::

  children                          childNodes
  childElementCount                 childNodes.length
  firstElementChild                 firstChild
  lastElementChild                  lastChild
  nextElementSibling                nextSibling
  previousElementSibling            previousSibling

现代浏览器（包括IE8）中document.querySelectorAll('#menu a')，不会随document而自动更新，比自己构建快3倍左右

querySelector返回第一个

浏览器完成下载后，会创建DOM tree和render tree，其中hidden DOM elements不会出现在render tree中.
DOM改变如果对元素尺寸有影响，浏览器会重新计算该元素以及相关元素的render tree，即reflow；然后重绘该部分，即repaint.
如果没有影响尺寸，如更改背景色，则没有reflow，只有repaint.
reflow和repaint非常昂贵，会使得界面无法交互.

为优化性能，浏览器会自动将多个变化排队进行批量处理，
但是如果用户要取得layout信息（无论与变化元素有无关系），都会发生强制的重绘，从而在各浏览器中导致性能的略微下降，
因此在变化过程中尽量不使用以下方法::

  offsetTop, offsetLeft, offsetWidth, offsetHeight
  scrollTop, scrollLeft, scrollWidth, scrollHeight
  clientTop, clientLeft, clientWidth, clientHeight
  getComputedStyle() (currentStyle in IE)

特别注意如果有timeout异步查询layout时，很有可能会导致批量处理失效

尽量减少变化的数量

优化style::

  var el = document.getElementById('mydiv');
  el.style.borderLeft = '1px';
  el.style.borderRight = '2px';
  el.style.padding = '5px';

优化为::

  el.style.cssText = 'border-left: 1px; border-right: 2px; padding: 5px;';

也可以直接更改className::

  el.className = 'active';

优化dom::

  1.先隐藏，然后更改，然后显示
  var ul = document.getElementById('mylist');
  ul.style.display = 'none';
  appendDataToElement(ul, data);
  ul.style.display = 'block';

  2.使用document fragment（推荐）
  var fragment = document.createDocumentFragment();
  appendDataToElement(fragment, data);
  document.getElementById('mylist').appendChild(fragment);

  3.clone node
  var old = document.getElementById('mylist');
  var clone = old.cloneNode(true);
  appendDataToElement(clone, data);
  old.parentNode.replaceChild(clone, old);

将获取的尺寸尽量保存为内部变量，减少重复查询

避免小范围的更改引起大范围的重绘::

  使用absolute position脱离文档流，然后动画，最后恢复position使得整体重绘

IE7之后的:hover可以应用到任何元素，但是如果应用元素过多，会导致严重的性能问题。常见于大table中使用tr:hover改变背景色

利用事件代理减少事件绑定::

  <ul id="menu"><li><a href="menu1.html">menu #1</a></li></ul>

不支持js则直接跳转页面，支持js则调用ajax局部刷新::

  document.getElementById('menu').onclick = function(e) {
      // x-browser target
      e = e || window.event;
      var target = e.target || e.srcElement;
      var pageid, hrefparts;
      // only interesed in hrefs
      // exit the function on non-link clicks
      if (target.nodeName !== 'A') {
          return;
      }
      // figure out page ID from the link
      hrefparts = target.href.split('/');
      pageid = hrefparts[hrefparts.length - 1];
      pageid = pageid.replace('.html', '');
      // update the page
      ajaxRequest('xhr.php?page=' + id, updatePageContents);
      // x-browser prevent default action and cancel bubbling
      if (typeof e.preventDefault === 'function') {
          e.preventDefault();
          e.stopPropagation();
      } else {
          e.returnValue = false;
          e.cancelBubble = true;
      }
  };


CHAPTER 4 Algorithms and Flow Control
----------------------------------------

for in比其他循环方式慢7倍，不要用于array循环

优化循环的方法为减少每次的工作量和减少循环次数

原始::

  for (var i=0; i < items.length; i++){

避免重复计算length::

  for (var i=0, len=items.length; i < len; i++){

反向循环，省掉比较操作，速度更快，缺点是次序颠倒，可读性下降::

  for (var i=items.length; i--; ){

Duff’s Device可以用来减少循环次数，即在每次循环中执行多步循环操作::

  //credit: Jeff Greenberg
  var iterations = Math.floor(items.length / 8),
      startAt    = items.length % 8,
      i          = 0;
  do {
      switch(startAt){
          case 0: process(items[i++]);
          case 7: process(items[i++]);
          case 6: process(items[i++]);
          case 5: process(items[i++]);
          case 4: process(items[i++]);
          case 3: process(items[i++]);
          case 2: process(items[i++]);
          case 1: process(items[i++]);
      }
      startAt = 0;
  } while (--iterations);

直接展开甚至会更快::

  //credit: Jeff Greenberg
  var i = items.length % 8;
  while(i){
      process(items[i--]);
  }
  i = Math.floor(items.length / 8);
  while(i){
      process(items[i--]);
      process(items[i--]);
      process(items[i--]);
      process(items[i--]);
      process(items[i--]);
      process(items[i--]);
      process(items[i--]);
      process(items[i--]);
  }

超过1000的循环才会比较明显

原生的forEach虽然好用，但是效率上可能比较慢

两者比较或者不同类型值比较实用if-else，如果数量比较多用switch。switch效率比较高

最常发生的情况放到前面

在数量比较多时，loopup table更快

浏览器有call stack size的限制，如果迭代不好可能会超出从而引发异常提示，可以使用try-catch捕获
可以使用循环来代替迭代，使用memoization

Chapter 6 Responsive Interfaces
-----------------------------------

js代码和UI更新（例如按钮按下）以队列的形式在浏览器UI线程中依次执行

浏览器对js代码的最长运行时间有限制，在超过后会进行提示，最好的解决方案就是减少js代码运行时间，可以采用setTimeout或setInterval的方式。

100ms以下的延迟用户几乎无法察觉

windows中的setTimeout时间的偏移幅度为15ms，因此如果低于15ms可能会造成IE浏览器锁住

对于不要求同步和顺序执行的耗时循环，可以使用对数组分片，延迟执行的方式，来给予UI更新，避免浏览器假死

原始::

  for (var i=0, len=items.length; i < len; i++){
    process(items[i]);
  }

优化为::

  function processArray(items, process, callback) {
    var todo = items.concat();

    setTimeout(function f() {
      process(todo.shift());
      if (todo.length > 0) {
        setTimeout(f, 25);
      } else {
        callback(items);
      }
    }, 25);
  }

调用::

  var items = [123, 789, 323, 778, 232, 654, 219, 543, 321, 160];

  function outputValue(value) {
    console.log(value);
  }
  processArray(items, outputValue, function() {
    console.log("Done!");
  });

对于包含多个步骤的大任务，可以通过分解步骤的方法，将所有步骤放到数组中，然后采用数组延迟的方法进行优化

在每次延迟中执行尽可能多的任务片，取50ms，可以大幅度减少整体运行时间::

  var start = +new Date();
  do {
    process(todo.shift());
  } while (todo.length > 0 && (+new Date() - start < 50));


+new Date()

1s以上延迟的timer不会对响应造成影响，但是多个高频率的timer会导致系统反应显著变慢，因此建议仅仅使用一个timer，完成所有操作

对于不容易分片的耗时任务，例如大量json解析，可以使用Web Worker

每个worker使用自己的线程，不会影响UI线程的正常响应

通过onmessage(event)，postMessage来进行UI与worker，或者worker之间的通信，传递格式可以为object，Array和基本类型

Chapter 7 Ajax
------------------------------------

readyState === 3 在接收过程中响应事件，可以更快的做出反应，但是IE6,7不支持

multipart XHR通过一个HTTP请求中返回多种数据，缺点是没有缓存

如果只想发送数据，例如发送log，可以使用beacons方法，这是最快的，而且不会更改客户端::

  var url = '/status_tracker.php';
  var params = [
      'step=2',
      'time=1248027314'
  ];
  (new Image()).src = url + '?' + params.join('&');

IE8以上支持xpath，但是不太完整

jsonp不需要parse时间，因此比json更快

当用户CPU比带宽更重要时直接传输html

如果要自定义格式，可以使用chr(1)（\u0001）之类的ASCII字符作为分隔符

浏览器缓存ajax请求::

  client使用GET请求，服务端设置Expires header


Chapter 8 Programming Practices
----------------------------------------

四种解析字符串的方法，会创建新的编译环境，所以非常慢。因此避免使用eval和Function，setTimeout和setInterval使用匿名函数::

  var num1 = 5,
  num2 = 6,

  result = eval("num1 + num2"),
  sum = new Function("arg1", "arg2", "return arg1 + arg2");
  setTimeout("sum = num1 + num2", 100);
  setInterval("sum = num1 + num2", 100);

使用Object/Array字面量会更方便更快

消除重复判断的两种方法：lazy loading和Conditional Advance Loading

lazy loading在首次执行时重新定义该函数。这种方法初次执行较慢，适合不立即使用的场合::

  function addHandler(target, eventType, handler) {
    //overwrite the existing function
    if (target.addEventListener) {
      //DOM2 Events
      addHandler = function(target, eventType, handler) {
        target.addEventListener(eventType, handler, false);
      };
    } else {
      //IE
      addHandler = function(target, eventType, handler) {
        target.attachEvent("on" + eventType, handler);
      };
    }
    //call the new function
    addHandler(target, eventType, handler);
  }

Conditional Advance Loading适用于立即使用的场合::

  var addHandler = document.body.addEventListener ?
                  function(target, eventType, handler) {
                    target.addEventListener(eventType, handler, false);
                  } : function(target, eventType, handler) {
                    target.attachEvent("on" + eventType, handler);
                  };


10进制 -> 2进制::

  var num1 = 25,
  alert(num1.toString(2)); //"11001"

位运算::

  and	&
  or	|
  xor	^
  not ~

判断奇偶::

  传统：i%2
  位：i & 1


bitmask，常用于多个布尔型选项::

  var a = 1,
    b = 2,
    c = 4,
    d = 8;
  //所有可能的属性
  var options = a | c | d;
  //c在options中
  if (options & c) {}

优先使用原生方法

* Math库
* 用于CSS查询的querySelector() and querySelectorAll()

CHAPTER 9 Building and Deploying High-Performance JavaScript Applications
------------------------------------------------------------------------------

可用工具Apache Ant,Rake,make

js打包，目的是减少HTTP request数量，需要注意打包顺序来保持依赖

js预处理，可以借助C preprocessor (cpp)，使用指定宏进行处理，例如::

  #ifdef DEBUG
  (new YAHOO.util.YUILoader({
    require: ['profiler'],
    onSuccess: function(o) {
      YAHOO.tool.Profiler.registerFunction('foo', window);
    }
  })).insert();
  #endif

js最小化，目的是减少文件体积，增加下载速度，同时也鼓励写更多的注释
JSMin 去掉注释和空格
YUI Compressor 压缩率更高。用更短的变量名，去掉不必要的符号，例如::

  foo["bar"] ->foo.bar
  {"foo":"bar"} -> {foo:"bar"}
  'aaa\'bbb' ->  "aaa'bbb"
  "foo"+"bar" ->  "foobar"

写法影响压缩率。
例如使用内部变量指代objects/values，使用闭包，使用常量代替字符，
避免使用eval，Function，以及setTimeout，setInterval的字符串函数，with关键字::

  function toggle (element) {
    var YUD = YAHOO.util.Dom, className = "selected";
    if (YUD.hasClass(element, className)){
      YUD.removeClass(element, className);
    } else {
      YUD.addClass(element, className);
    }
  }

但是可能会影响zip后的文件大小，对性能也可能会产生不好影响，因此不要滥用。

Closure Compiler 更高级，更激进.
在firefox中提供Closure Inspector来对源文件进行映射进而调试，但是如果其他浏览器出现问题则不好调试

everything that can be done at buildtime should not be done at runtime


js压缩

浏览器request时通过Accept-Encoding通知web server浏览器支持什么编码的数据.
可能值为gzip, compress, deflate等

服务器选择最适合的编码方式，通过Content-Encoding通知浏览器::

  Content-Encoding:gzip

gzip主要用于text，包括js的压缩.
图片，pdf等已经被压缩过了，因此不需要gzip

Apache mod_gzip/mod_deflate

Packer可以进一步压缩，但是在运行时会有速度损耗；通常用于不支持gzip的慢速链接中。

通常情况下YUI Compressor+gzip已经足够.

js缓存

可以显著提升加载速度.
应该被应用于所有静态文件，包括js，images等

服务器通过Expires response header告诉浏览器存储时间::

  Expires: Thu, 01 Dec 1994 16:00:00 GMT

根据规范，不应该设置一年以上的过期时间

需要注意有些手机浏览器对cache有限制，例如iphone上的safari不能缓存25kb以上的数据，因此需要对其优化

使用浏览器存储，通过js控制过期

HTML 5 offline application cache,
a manifest file listing the resources to be cached::

  <!DOCTYPE html>
  <html manifest="demo.manifest">


通过自动添加timestamp的方式改名，来更新被缓存的文件

使用CDN实现性能，扩展，稳定::

  yui.yahooapis.com
  ajax.googleapis.com

部署

复制多个文件到多个远程主机，运行一系列命令，CDN分发

FTP SCP ssh
