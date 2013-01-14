.. _raphael:

***************
raphael
***************

记录
==========
transform，path参数可以为字符串或数组

b.attr('path')
chrome下返回值为path数组，IE下为字符串

path绘制::

  C	三次曲线	(x1 y1 x2 y2 x y)+
  S	平滑三次曲线	(x2 y2 x y)+
  Q	二次曲线	(x1 y1 x y)+
  T	平滑二次曲线，貌似要用在Q后面	(x y)+
  A	elliptical arc	(rx ry x-axis-rotation large-arc-flag sweep-flag x y)+
  R	Catmull-Rom curveto*	x1 y1 (x y)+
