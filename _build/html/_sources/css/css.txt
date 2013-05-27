.. _css:


***************
css
***************

技巧
--------

[type=text] 与 .invalid 优先级一样

IE9以下不支持linear-gradient

outline比较border而言不占位置

disabled在IE6也可以使得input不可输入


缩进2字符::

  text-indent: 2em;

使用很大的line-height实现文字隐藏::

  line-height: 100px;

设置最大高度，超过则出现滚动条::

  max-height: 80px;
  overflow: auto;

垂直对齐使用 vertical-align，只应用于inline level, inline-block level 及 table-cells 元素上。

hsl::

  svg中设置
    fill:'hsl(72deg,1,.37)'

  css中设置
    background: hsl(72,100%,37%);

div:after 相当于在div里加入一个标签，放到最后，content设置内容。before放到最前。


基本属性
-------------

white-space控制空格以及是否换行::

  normal (默认)多个空格合并为一个，自动换行，但是回车不换行
  nowrap 多个空格合并为一个，不换行（除非<br/>）
  pre 保留空格，回车换行
  pre-line 多个空格合并为一个，自动换行，回车换行
  pre-wrap 保留空格，自动换行，回车换行

word-wrap::

  normal （默认）
  break-word 连续字母切断换行


基本概念
----------

stacking context
==================

https://developer.mozilla.org/zh-CN/docs/CSS/Understanding_z-index/The_stacking_context

形成条件：

* root emement(HTML)
* position为absolute或relative，z-index不为auto
* opacity小于1
* mobile webkit或chrome22+，position:fixed，即使z-index:auto

block vs inline
==================

默认

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
==================

脱离文档流的方法::

  float:left/right
  postion:absolute/fixed

从性能上看，将元素的position设置为absolute和fixed可以使元素从DOM树结构中脱离出来独立的存在，
而浏览器在需要渲染时只需要渲染该元素以及位于该元素下方的元素，从而在某种程度上缩短浏览器渲染时间。
所以如果是制作js动画等，用absolute或者fixed定位会更好。

不推荐用position来布局整个页面的大框架，而推荐用float或者文档流的默认方式。

取代float方式布局::

  display:inline-block; /* 现代浏览器 +IE6、7 inline 元素 */
  *display:inline; /* IE6、7 block 元素 */
  *zoom:1;

yui grid: http://yui.yahooapis.com/3.3.0/build/cssgrids/grids.css

inline-block 前世今生: http://ued.taobao.com/blog/2012/08/15/inline-block/

position
~~~~~~~~~~

* static  默认值。在正常流中，没有定位，忽略 top, bottom, left, right 或者 z-index 声明
* relative  相对于正常位置定位
* absolute  相对于static之外的第一个父元素定位
* fixed  相对于浏览器窗口进行定位。

position:absolute中的width，height是相对父relative来定义的

float vs inline-block
=========================

inline-block 内部像block，可以设置width, height, padding, border与margin。
外部的排列方式像行内元素，即水平排列，而不是像块级元素一样从上到下排列

相同点：
内部表现为块级元素，水平排列

区别：

1. 文档流（Document flow）:浮动元素会脱离文档流，并使得周围元素环绕这个元素。
   而inline-block元素仍在文档流内。因此设置inline-block不需要清除浮动。
#. 水平位置（Horizontal position）：很明显你不能通过给父元素设置text-align:center让浮动元素居中。
   事实上定位类属性设置到父元素上，均不会影响父元素内浮动的元素。
   但是父元素内元素如果设置了display：inline-block，则对父元素设置一些定位属性会影响到子元素。
#. 垂直对齐（Vertical alignment）：inline-block元素沿着默认的基线对齐。浮动元素紧贴顶部。
   你可以通过vertical属性设置这个默认基线，但对浮动元素这种方法就不行了。这也是我倾向于inline-block的主要原因。
#. 空白（Whitespace）：inline-block包含html空白节点。
   如果你的html中一系列元素每个元素之间都换行了，当你对这些元素设置inline-block时，这些元素之间就会出现空白。
   而浮动元素会忽略空白节点，互相紧贴
#. IE6和IE7：Ie67对inline-block的兼容性问题。

解决空白问题：

* 删除html中的空白：不要让元素之间换行
* 使用负边距：你可以用负边距来补齐空白。但你需要调整font-size，因为空白的宽度与这个属性有关系。
* 给父元素设置font-size:0：不管空白多大，由于空白跟font-size的关系，设置这个属性即可把空白的宽度设置为0，
  还需要给子元素重新设置font-size。

使用场景：
如果你需要文字环绕容器，那浮动是不二选择。如果你需要居中对齐元素，inline-block是个好选择。

* 使用inline-block：当你需要控制元素的垂直对齐跟水平排列时（例如不固定高度图片排列），使用inline-block。
* 使用浮动：当你需要让元素环绕某一个元素时，或者不想处理inline-block带来的空白问题时，使用浮动。

BFC vs hasLayout
==================

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
~~~~

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
~~~~~~~~~~~~

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

layout元素设置display: inline 相当于通常意义上的inline-block

相同点
~~~~~~~~~~~~~~~

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

不同点
~~~~~~~~~~~~~~~

1.触发haslayout的元素是可以设置宽高的，而触发BFC的元素不一定可以设置宽高
比如一个行内元素，设置float或者设置overflow都可以触发BFC，但是前者可以设置宽高，后者却不能

2.hasLayout的元素设置display:inline后与inline-block行为类似,
用来解决IE6/7下inline-block问题::

  display:inline-block;
  *display:inline;
  *zoom:1;

浏览器预设样式
------------------

chrome
===========

button 有默认的margin:2px

HTML5 Doctype下，如果div包含img，div会自动增加4px的bottom margin::

  原因：这是为了方便在div中直接添加text
  解决方法：div设置line-height:0; 或者 img设置display:block;

编译
-------

less
=======

使用less实现修改样式后页面自动刷新，在console中::

  less.watch()

颜色减淡::

  +#111

sass
==================

实时编译为css::

  sass --watch your/scss/directory:your/css/directory

框架和库
------------

jqueryui
=========

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

bootstrap
============

* .badge比.label边角更圆一些

* .hero-unit显示页面主要内容，里面的h1，p等都调大了

* .page-header用于显示标题，有下边线

  h1>small显示补充信息

* .thumbnails用于图片展示，产品简介等，ul > li即可

  其中的li如果设置.span3会使得img按比例缩放

  .thumbnail使用border-radius设置圆角，box-shadow设置立体感，padding使得img留有白边。

* .progress-striped使用gradient来实现斜条纹，可使用工具 http://www.colorzilla.com/gradient-editor/

关闭按钮::

  <a class="close" href="#">&times;</a>

background-clip 和 background-origin用来确定背景的定位

btn心跳闪烁::

  @-webkit-keyframes downloadButton {
    from { box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 5px rgba(0,0,0,.25), 0 2px 10px rgba(0,68,204,.5); }
    50% {  box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 5px rgba(0,0,0,.25), 0 2px 25px rgba(0,68,204,.9); }
    to {   box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 5px rgba(0,0,0,.25), 0 2px 10px rgba(0,68,204,.5); }
  }
  @-moz-keyframes downloadButton {
    from { box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 5px rgba(0,0,0,.25), 0 2px 10px rgba(0,68,204,.5); }
    50% {  box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 5px rgba(0,0,0,.25), 0 2px 25px rgba(0,68,204,.9); }
    to {   box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 5px rgba(0,0,0,.25), 0 2px 10px rgba(0,68,204,.5); }
  }
  .btn {
    -webkit-animation-name: downloadButton;
       -moz-animation-name: downloadButton;
    -webkit-animation-duration: 1.5s;
       -moz-animation-duration: 1.5s;
    -webkit-animation-iteration-count: infinite;
       -moz-animation-iteration-count: infinite;
  }

* fluid grid(.row-fluid)在屏幕大于960px时会继续扩大，而fixed grid(.row)不会改变
* responsive会根据media query在某宽度时更改大小，在屏幕很小时从float改为stack

::

  .leftHalf{ width: 50%; float: left}
  .rightHalf{ width: 50%; float: left }

  @media (max-width: 320px){
      .leftHalf{ width: 100%; color: red; }
      .rightHalf{ width: 100%; color: blue; }
  }

foundation
===========

box-sizing: border-box 简化width的计算

768px为分隔

grid
~~~~~~~

row::

  .row 整行

    width: 100%; //窄屏100%宽度
    max-width: 62.5em; //宽屏固定大小
    margin: 0 auto; //居中

  嵌套row（.row .row ）

    width: auto;
    max-width: none;
    左右margin补偿columns的padding

columns::

  行中的列需要.columns，一行12列，如果超出12则显示为下一行

  position: relative; //为定位准备
  float: left; //左浮动
  有左右padding

  如果设置了多个column，最后一个右浮动。即如果不满足12实现两端浮动效果
  [class*="column"] + [class*="column"]:last-child {
    float: right;
  }


  .large-* 设置宽屏中比例，如果只设large-*则窄屏中显示为整行
  .small-* 设置窄屏中比例，如果只设small-*则宽屏中也按该比例显示
  百分比宽度


  .show-for-small 在窄屏中显示
  .hide-for-small 在宽屏中显示
  如果不设置则宽屏窄屏中都显示

  .large-offset-* 和 .small-offset-* 通过margin-left进行偏移


  small-centered 窄屏中整行居中，宽屏中无居中效果，也没有偏移
  large-centered 宽屏中整行居中，窄屏中无效

  .push-* 宽屏中通过设置百分比left将元素推向右边
  .pull-* 宽屏中通过设置百分比right将元素拉向左边

功能
~~~~~~~

* orbit 图片文字走马灯
* clearing 图片点击灯箱效果
* dropdown 下拉条
* joyride 自动游览页面
