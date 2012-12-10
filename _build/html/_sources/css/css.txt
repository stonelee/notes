.. _css:


***************
css
***************

缩进2字符::

  text-indent: 2em;

左中定宽，右自适应方法：左中float:left，右margin-left

貌似可以取代float::

  display: inline-block;
  *display: inline;
  *zoom: 1;


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

float vs position
-----------------------

从性能上看，将元素的position设置为absolute和fixed可以使元素从DOM树结构中脱离出来独立的存在，
而浏览器在需要渲染时只需要渲染该元素以及位于该元素下方的元素，从而在某种程度上缩短浏览器渲染时间。
所以如果是制作js动画等，用absolute或者fixed定位会更好。

不推荐用position来布局整个页面的大框架，而推荐用float或者文档流的默认方式。


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

hasLayout和BFC
-----------------------------

因为CSS的模型和术语脱胎于传统排版，故而与计算机GUI技术通常基于组件的模型相差甚远。
除了float之外，另一个例子是CSS中上下margin的collapse，显然这是为了满足段落排版的需求。
所以像float、margin collapse等，在典型的GUI技术中是没有的。
还有，CSS box model中，width/height不算入padding和border，许多开发者对这点很不适应，这实际上是GUI的控件思维与CSS排版思维的冲突。
这个冲突在浏览器技术实现上的遗迹就是IE臭名昭著的“hasLayout”。
元素“has layout”的真实意思是这样的元素直接对应一个控件。
也正是由于IE很naive的在实现中直接结合了这两种矛盾的模型，从而导致了无数的布局bug。 


block formatting context	块级元素格式上下文
hasLayout			IE5.5/6/7上一些奇怪的bug

::

  overflow:hidden	触发BFC
  *zoom:1			触发hasLayout

设置float		触发BFC

IE中跟尺寸有关的bug往往可以通过layout设置width或者height来解决

zoom: 1 //IE特有属性来激发layout

layout元素设置display: inline 相当于通常意义上的inline-block

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

渐进增强与平稳退化
----------------------

平稳退化 (Graceful Degradation)于1994 年提出，由于其并不真正互联网符合普及的可访问型 Web (Universally Accessible Web)”的设计初衷。2003 年提出渐进增强 (Progressive Enhancement)，聚焦于内容并能为旧设备提供更多实际支持，从而改善内容可利用性 (Content Availability)、全局可访问性 (Overall Accessibility) 和移动设备浏览器的能力。


它们是看待同种事物的两种观点，都关注于同一网站在不同设备里不同浏览器下的表现程度。关键的区别则在于它们各自关注于何处，以及这种关注如何影响工作的流程。


"平稳退化”观点认为应该针对那些最高级、最完善的浏览器来设计网站。而将那些被认为“过时”或有功能缺失的浏览器下的测试工作安排在开发周期的最后阶段，并把测试对象限定为主流浏览器（如 IE、Mozilla 等）的前一个版本。在这种设计范例下，旧版的浏览器被认为仅能提供“简陋却无妨 (poor, but passable)” 的浏览体验。你可以做一些小的调整来适应某个特定的浏览器。但由于它们并非我们所关注的焦点，因此除了修复较大的错误之外，其它的差异将被直接忽略。


“渐进增强”观点则认为应关注于内容本身.即从内容出发。内容为样式和交互构建起坚实的基础，由上至下分别为：“内容”、“表现”和“客户端脚本”。

这种开发方式被称为“无侵入 (Unobtrusive)

渐进增强实例
===============

文字阴影：text-shadow: 1px 1px white;（右下白色阴影）

圆角：border-radius: 3px; （按钮3px，文本框6px）

盒阴影：box-shadow: 1px 2px 3px rgba(0, 0, 0, .5);（右下透明阴影）

渐变背景: background:-moz-linear-gradient(top , #F2F2F2, #ffffff 8px);（按钮、标题栏、控件背景）

CSS选择器、伪类：li:first-child{border-top:0;}（去掉第一个li的top border）

input:focus {border-color:#a0b3d6;}（IE6、7不支持）

text-overflow：ellipsis （文字溢出特定宽度“点点点”省略号表示）

CSS3
----------

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


less
-----------

使用less实现修改样式后页面自动刷新，在console中::

  less.watch()

颜色减淡::

  +#111

jqueryui
-----------

合并顺序::

  base
    -- core 最核心不变的
    -- accordion
    -- ...
    -- tooltip

  theme 易变，特别指定
    font-family, font-size,
    ui-widget-content -- border, background, color, font-weight
             -header
    state, corner, overlay, shadow

css如果为一个元素指定多个class，其优先级取决于css文件中的定义顺序，后定义的会覆盖前面定义的。与class的书写顺序无关

class顺序与实际样式表顺序一致，方便查询

开发顺序：

* 功能实现
* 抽象架构，着眼于扩展
