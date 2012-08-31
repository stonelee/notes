.. _bootstrap:


***************
bootstrap
***************

* .label

  white-space: nowrap; 防止换行

  通过background-color区分不同

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

