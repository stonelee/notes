.. _css:


***************
css
***************


position:absolute中的width，height是相对父relative来定义的

em 强调

* a>img
* li>a
* h4>a

image调整垂直位置:vertical-align

position
--------------------

* static	在正常流中，忽略left等
* relative	相对于正常位置定位
* absolute	相对于static之外的第一个父元素定位

block formatting context
-----------------------------

产生条件：

* float not 'none': left, right
* overflow not 'visible': hidden, scroll, auto
* display: 'table-cell', 'table-caption', or 'inline-block'
* position:absolute, fixed 

位于normal flow

效果：

1. prevent margin collapsing

	位于相同block formatting context中的相邻block boxes会对vertical margins折叠

	消除方法::

		overflow:hidden;zoom:1

	或者设置 border or padding

#. Block formatting contexts contain floats


字体
---------

字体分为三类（generic family）：Serif、Sans-serif、Monospace

Serif对某些字符笔画末端加了些小短线做装饰

在计算机屏幕上Sans-serif比Serif更易读

16px=1em

W3C推荐使用em来代替px，因为px在IE9之前版本中无法随页面缩放，
但是em在IE老版本中缩放比例不一致，所以body {font-size:100%;}，然后再使用em

font-size/line-height, font-family将generic family放到最后面，来自动选择此类型的字体::

	font: 12px/18px "Lucida Grande", "Lucida Sans Unicode", Arial, sans-serif;


CSS3
=================

阴影box-shadow::

	横偏移 竖偏移 阴影大小 颜色	
	-webkit-box-shadow:0 15px 10px rgba(0, 0, 0, 0.7);
	-moz-box-shadow:0 -15px 10px rgba(0, 0, 0, 0.7);
	box-shadow:10px 15px 10px rgba(0, 0, 0, 0.7);

旋转transform::

	-3逆时针
	-webkit-transform:rotate(-3deg);
	-moz-transform:rotate(-3deg);
	-o-transform:rotate(-3deg);
	transform:rotate(-3deg);


