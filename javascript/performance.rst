.. _performance:

******************
高性能JavaScript
******************

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
