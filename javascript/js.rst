.. _js:

***************
js
***************

技巧
=============================

判断为list，而不是object::

	if (obj.length === +obj.length) {}

* object.length	undefined
* +obj.length	NaN

::

	lst = ['a','b','c']
	2 in lst	true

breaker用作模块内部的标记，外面无法修改::

	var breaker={};
	console.log({}===breaker);	false

lst.length=8	会扩展array长度，不足的为undefined

::

	//else false
	if (a=false){
		console.log(a);
	}
	else {
		console.log('else',a);
	}

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

undefined==null

for (var key in dict)

l.length=0	清空array

::

	> lst = [];
	> if (lst) console.log(true);
	true

arg.length说明可以$.each

[]会被认为是true

document.documentMode
---------------------------

* 5	Internet Explorer 5 mode (also known as "quirks mode").
* 7	Internet Explorer 7 Standards mode.
* 8	Internet Explorer 8 Standards mode.
* 9	Internet Explorer 9 Standards mode.
* 10	Internet Explorer 10 Standards mode.

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
	alert(iNum.toString(2));	//输出 "10010"

位运算 NOT 实质上是对数字求负，然后减 1，因此 25 变 -26

escape
-----------

* escape()	已经被废弃，不要使用
* encodeURI()	url编码，编码后仍然可以使用
* encodeURIComponent()	作为url参数编码使用

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
	console.log(Foo.prototype.constructor===Foo);// true
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

思考
=============================

搞清组件的核心功能，果断调用。如jQuery为DOM/Ajax/Anim 操作类库

对于非核心功能，可以考虑在自己组件里实现。如$.extend 或 $.each

IE6/7不支持JSON，需要借助json2.js，其他版本原生支持

async
=============================

将多层嵌套变为一层，还是需要callback

js库
=============================

多选控件，包括自动补全，ajax等功能
http://textextjs.com/

类似iphone的手指滑动，滚动屏幕效果
http://natrixnatrix89.github.com/promptu-menu/
