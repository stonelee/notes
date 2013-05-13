.. _ie6:


***************
IE6
***************

hack
-------------

::

  #Holly hack
  /* \*/
  * html .gainlayout { height: 1%; }
  /* */

  #underscore hack:
  .gainlayout { _height: 0; }


问题
---------

IE6中同一个大括号中的重复属性，后面的将会覆盖前面的，不管前面的属性是否有!important；
而在不同的大括号里，则有!important的属性有效

单线table::

  border-collapse: collapse;//IE6中需要
  border-spacing: 0;

IE6中使用background-position指定图片，即使设置height也会撑大，这时可以设置overflow:hidden来避免

父容器position:relative;容易在IE6中出现各种问题，如子元素的border-top不显示等。解决方法是加上*zoom:1

border: 1px solid transparent;

非a元素的hover .icon-btn:hover

32-bit alpha-transparent PNG::

  使用Fireworks save your alpha-tranparent PNG image in 8-bit format,

IE6中如果使用 <!DOCTYPE> 就可以使用正确的盒模型

min-height for IE6::

  div.min-height {
    min-height: 500px;
    height: auto !important;
    height: 500px;
  }

max-width,min-width,max-height需要使用expression，问题在于速度慢，借助js实现::

  /* max-width for IE6 */
  * html div.max-width {
    width: expression(document.body.clientWidth > 776 ? "777px" : "auto");
  }
  /* max-width for standards-compliant browsers */
  div.max-width {
    max-width: 777px;
  }

double margin bug
=====================

float an element (such as a <div>) in one direction and then apply a margin in that same direction::

  div#selector {
    float: right;
    margin-right: 10px;
  }
  * html div#selector {
    display: inline; /* kill double-margin bug */
  }
