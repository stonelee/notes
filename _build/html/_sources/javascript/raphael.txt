.. _raphael:

***************
raphael
***************

源码
==========

::

  R.fn = paperproto = Paper.prototype = R.prototype;
  R.el = elproto = Element.prototype;

记录
==========

Element.transform([tstr])::

  参数可以为字符串或数组
  t - translate, r- rotate, s -scale, m -matrix
  大写为绝对变形

  t100,100(translate by 100, 100)
  r30,100,100(rotate 30° around 100, 100)
  s2,2,100,100(scale twice around 100, 100)
  r45(rotate 45° around centre)
  s1.5(scale 1.5 times relative to centre)

不要使用translate等函数，在setViewBox后不同浏览器中的返回值可能不一样。
使用transform(['t',10,10])来替代

b.attr('path') 在chrome下返回值为path数组，IE下为字符串

path绘制::

  C	三次曲线	(x1 y1 x2 y2 x y)+
  S	平滑三次曲线	(x2 y2 x y)+
  Q	二次曲线	(x1 y1 x y)+
  T	平滑二次曲线，貌似要用在Q后面	(x y)+
  A	elliptical arc	(rx ry x-axis-rotation large-arc-flag sweep-flag x y)+
  R	Catmull-Rom curveto*	x1 y1 (x y)+

问题
========

vml中图片放大两倍（size，position）时内存占用也会变为两倍
<rvml:fill class=rvml rotate="t" src="mine.png" type="tile" size="3200,2400" position="-1600,-1200"></rvml:fill>

IE下setViewBox是对每个元素进行控制，速度太慢，还是换回ASV吧
