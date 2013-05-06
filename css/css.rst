.. _css:


***************
css
***************

white-space控制空格以及是否换行::

  normal (默认)多个空格合并为一个，自动换行，但是回车不换行
  nowrap 多个空格合并为一个，不换行（除非<br/>）
  pre 保留空格，回车换行
  pre-line 多个空格合并为一个，自动换行，回车换行
  pre-wrap 保留空格，自动换行，回车换行

word-wrap::

  normal （默认）
  break-word 连续字母切断换行


stacking context::

  https://developer.mozilla.org/zh-CN/docs/CSS/Understanding_z-index/The_stacking_context

  形成条件：
  root emement(HTML)
  position为absolute或relative，z-index不为auto
  opacity小于1
  mobile webkit或chrome22+，position:fixed，即使z-index:auto

缩进2字符::

  text-indent: 2em;

使用很大的line-height实现文字隐藏::

  line-height: 100px;

设置最大高度，超过则出现滚动条::

  max-height: 80px;
  overflow: auto;

em 强调

* a>img
* li>a
* h4>a

image调整垂直位置:vertical-align

hsl::

  svg中设置
    fill:'hsl(72deg,1,.37)'

  css中设置
    background: hsl(72,100%,37%);

div:after 相当于在div里加入一个标签，放到最后，content设置内容。before放到最前。

垂直对齐使用 vertical-align，只应用于inline level, inline-block level 及 table-cells 元素上

默认元素
-----------------

block::

  div
  p
  h1 h2 h3 h4 h5 h6

  table
  fieldset
  form
  ul - 非排序列表
  ol - 排序表单
  dl - 定义列表

  blockquote - 块引用
  hr - 水平分隔线
  address - 地址
  pre - 格式化文本

inline::

  a
  span - 常用内联容器，定义文本内区块
  em - 强调
  i - 斜体
  br - 换行

  img - 图片
  input - 输入框
  textarea - 多行文本输入框
  label - 表格标签

  sub - 下标
  sup - 上标
  big - 大字体
  small - 小字体文本
  strong - 粗体强调
  abbr - 缩写
  acronym - 首字
  cite - 引用
  code - 计算机代码(在引用源码的时候需要)
  dfn - 定义字段

float vs position
-----------------------

脱离文档流的方法::

  float:left/right
  postion:absolute/fixed

从性能上看，将元素的position设置为absolute和fixed可以使元素从DOM树结构中脱离出来独立的存在，
而浏览器在需要渲染时只需要渲染该元素以及位于该元素下方的元素，从而在某种程度上缩短浏览器渲染时间。
所以如果是制作js动画等，用absolute或者fixed定位会更好。

不推荐用position来布局整个页面的大框架，而推荐用float或者文档流的默认方式。

取代float方式布局::

  display: inline-block;
  *display: inline;
  *zoom: 1;

yui grid: http://yui.yahooapis.com/3.3.0/build/cssgrids/grids.css

inline-block 前世今生: http://ued.taobao.com/blog/2012/08/15/inline-block/

position
============

* static  在正常流中，忽略left等
* relative  相对于正常位置定位
* absolute  相对于static之外的第一个父元素定位

position:absolute中的width，height是相对父relative来定义的

hasLayout和BFC
-----------------------------

* block formatting context  块级元素格式上下文
* hasLayout                 IE5.5/6/7上一些奇怪的bug根源

最常用::

  overflow:hidden //触发BFC
  *zoom:1         //IE6中触发hasLayout

因为CSS的模型和术语脱胎于传统排版，故而与计算机GUI技术通常基于组件的模型相差甚远。
除了float之外，另一个例子是CSS中上下margin的collapse，显然这是为了满足段落排版的需求。
所以像float、margin collapse等，在典型的GUI技术中是没有的。
还有，CSS box model中，width/height不算入padding和border，这实际上是GUI的控件思维与CSS排版思维的冲突。
这个冲突在浏览器技术实现上的遗迹就是IE臭名昭著的“hasLayout”。
元素“has layout”的真实意思是这样的元素直接对应一个控件。
也正是由于IE很naive的在实现中直接结合了这两种矛盾的模型，从而导致了无数的布局bug。

BFC
==========

CSS 101: Block Formatting Contexts: http://www.yuiblog.com/blog/2010/05/19/css-101-block-formatting-contexts

产生条件：

* float不为none，可以为'left', 'right'
* overflow不为visible，可以为'hidden', 'scroll', 'auto'
* display为 'table-cell', 'table-caption', 'inline-block'
* position为'absolute', 'fixed'

效果：

1. 清浮动环绕
#. 清内部浮动影响
#. 清嵌套margin折叠


位于相同BFC中的相邻block boxes会对vertical margins折叠.
消除方法::

  overflow:hidden;*zoom:1

或者设置 border or padding


hasLayout
=============

更加直观地了解hasLayout和BFC: http://www.w3ctech.com/p/1101

On having layout: http://www.satzansatz.de/cssd/onhavinglayout.html

默认拥有layout的元素::

  <html>, <body>
  <table>, <tr>, <th>, <td>
  <img>
  <hr>
  <input>, <button>, <select>, <textarea>, <fieldset>, <legend>
  <iframe>, <embed>, <object>, <applet>
  <marquee>

属性触发::

  position: absolute
  float: left|right
  display: inline-block
  width: any value other than 'auto'
  height: any value other than 'auto'
  zoom: any value other than 'normal' （非标准，推荐使用）
  writing-mode: tb-rl

  #IE7可以使用
  overflow: hidden|scroll|auto
  overflow-x|-y: hidden|scroll|auto
  position: fixed
  min-width: any value
  max-width: any value other than 'none'
  min-height: any value
  max-height: any value other than 'none'

IE6 hack::

  #Holly hack
  /* \*/
  * html .gainlayout { height: 1%; }
  /* */

  #underscore hack:
  .gainlayout { _height: 0; }

layout元素设置display: inline 相当于通常意义上的inline-block

两者的相同点
===================

1.清浮动环绕

左右定宽，中间自适应::

  左float:left, 右float:right, 中间overflow:hidden来BFC

当然也可以不用::

  //左中定宽，右自适应
  左中float:left，右margin-left

左图右文，文字不环绕图::

  左float:left, 右BFC

2. 清内部浮动影响

父元素中设置，避免内部元素的float影响外面的元素::

  .outer{
      overflow:hidden;
      *zoom:1;
  }

当然也可以不用BFC::

  .clearfix:after {
    content: " ";
    display: block;
    clear: both;
    height: 0;
  }
  .clearfix {
    *height: 1%;//IE6，7
  }

3. 清嵌套margin折叠

父元素设置，使得嵌套元素的margin都能够奏效，
如果不设置的话会将嵌套元素边距折叠为最大的::

  .div1{
    overflow:hidden;
    *zoom:1;

    margin:20px;
    background:yellow;
  }
  .div2{
    width:50px;
    height:50px;

    margin:50px;
    background:red;
  }

两者的不同点
===============

1.触发haslayout的元素是可以设置宽高的，而触发BFC的元素不一定可以设置宽高
比如一个行内元素，设置float或者设置overflow都可以触发BFC，但是前者可以设置宽高，后者却不能

2.hasLayout的元素设置display:inline后与inline-block行为类似,
用来解决IE6/7下inline-block问题::

  display:inline-block;
  *display:inline;
  *zoom:1;

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

渐变背景: background:-webkit-linear-gradient(top , #F2F2F2, #ffffff 8px);（按钮、标题栏、控件背景）

CSS选择器、伪类：li:first-child{border-top:0;}（去掉第一个li的top border）

input:focus {border-color:#a0b3d6;}（IE6、7不支持）

text-overflow：ellipsis （文字溢出特定宽度“点点点”省略号表示）

图片渐入: -webkit-transition: all 0.3s ease-out 0s;

图片旋转: -webkit-transform: rotate(360deg);

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


pointer-events

设置该元素是否响应鼠标事件，设为none则元素不再是鼠标事件的目标，鼠标不再监听当前层而去监听下面层中的元素。
如果它的子元素设置为auto，鼠标还是会监听这个子元素的。
用于google地图的导航区域

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

浏览器预设样式
------------------

chrome
===========

button 有默认的margin:2px

HTML5 Doctype下，如果div包含img，div会自动增加4px的bottom margin::

  原因：这是为了方便在div中直接添加text
  解决方法：div设置line-height:0; 或者 img设置display:block;

