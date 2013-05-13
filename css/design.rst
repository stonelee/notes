.. _design:


***************
design
***************

Scheme
-------------

从图片中选取颜色，然后从色盘中选取邻近色和相反色。

配色方案设计的六种配色方案：

* 单色（单色配色）：以单一颜色做为基础色，再以饱合度，亮度变化出其它搭配的色。因为是属于同一个色系，所以这种配色法较能调配出舒适的色彩感受。
* 补充（互补色配色）：以主色以及在色环对面的补色调出对比效果明显的配色。
* 三合会（三分色配色）：以一个主色以及在色环对面的两个补色组成较为柔合的对比效果。
* 四分体（四分色配色）：以两个主色以及在色环对面的两个补色营造出一种强烈的视觉效果。
* 类比（类似色配色）：以一个主色以及在它两旁等距的两个补色调配出给人优雅，简洁的色彩感觉。
* 重音的类比（互补类似色配色）：以三个类似色为基础，再加上色环对面的一个对比色构成一种既不失优雅又能强调重点的有效配色法。

字体
---------

* serif(Times New Roman) 对某些字符笔画末端加了些小短线做装饰。适于印刷，不适于屏幕显示，尤其是小字体时，可以应用于大字体。
* Sans-serif(Arial, Helvetica, verdana)，适用于大量文字屏幕显示
* Monospace(Courier)，适用于代码显示或邮件中的发票（空格等宽便于对齐）

Microsoft Web Fonts::

  Arial, Courier New, Georgia, Times New Roman, Verdana

不同字体的height, width, x-height,descender height, ascender height都可能不同


16px=1em

W3C推荐使用em来代替px，因为px在IE9之前版本中无法随页面缩放，
但是em在IE老版本中缩放比例不一致，所以body {font-size:100%;}，然后再使用em

font-size/line-height, font-family将generic family放到最后面，来自动选择此类型的字体::

  font: 12px/18px "Lucida Grande", "Lucida Sans Unicode", Arial, sans-serif;


调整margin，padding为18的倍数来保证多列文字的水平对齐

imageMagick
---------------

gif批量转为png::

  mogrify -format png *.gif

单个png转为gif::

  convert tree-s7defbb4611.png tree-s7defbb4611.gif

compass的sprite只支持png格式，但是IE6不支持png透明

转为PNG-8，IE6支持，而且体积更小::

  convert tree-s7defbb4611.png -colors 256 PNG8:tree.png

将所有img00开头的文件进行合并，将白色设为透明背景，合并为1行，
每个文件大小为121*98，没有间隔，导出为png格式::

  montage img00*.jpg -background transparent -transparent #fff -tile x1 -geometry 121x98+0+0 player.png

image sprites::

  montage grid/* -background transparent -geometry '16x16+0+0>' grid.gif

图片格式
-----------

* gif 支持透明，支持动画，无损耗，水平扫描，间隔渐进显示，只有256种颜色，不适合照片，但它适合对颜色要求不高的图形（比如说图标，图表等）
* jpeg 不支持透明，不支持动画，有损耗，所以在编辑过程一般用png作为过渡格式。隔行渐进显示，适合web上面的摄影图片和数字照相机
* png 支持透明，不支持动画，无损耗，水平扫描，间隔渐进显示

结论::

  动画gif最好
  png8代替静态gif
  PNG24接近JPG，但因为是无损格式，同样尺寸的照片png24比jpg画质要高很多而且体积大很多，所以一般网站使用jpg

  PNG8除了不支持动画外和GIF基本一致，属于256的索引色，其中包括透明索引，不支持半透明
  PNG24即24位全彩，RGB三色各占8位(#FFFFFF,0xFFFFFF)，但不包含透明度，不过PS将PNG24和PNG32的概念整合到PNG24了，这点FW有明显的区分
  PNG32即32位全彩，ARGB四色各占8位(0xFFFFFFFF)，含alpha透明度

两种jpeg加载方式
===================

* 自上而下线性加载（基本）
* 先是全部的模糊图片，然后逐渐清晰（渐进）

两种图片大小差不多，加载速度方面渐进方式在现代浏览器中快的多，一开始就能定好大小，防止回流，但是占CPU、内存较多

水平扫描（gif，png）
======================

使用了一种叫作LZW的算法进行压缩，当压缩gif的过程中，像素是由上到下水平压缩的，
这也意味着同等条件下，横向的gif图片比竖向的gif图片更加小。例如500*10的图片比10*500的图片更加小
