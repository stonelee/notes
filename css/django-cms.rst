.. _django-cms:


***************
django-cms
***************

https://www.django-cms.org/

技巧
=====================

logo样式::

	<h1 class="logo_main">
		<a href="#" class="offset noprint">logo</a>
		<img src="media/img/logo_main.png" class="print" alt="some">
	</h1>

将两幅图合到一起，通过偏移来形成动态效果；float:left相当于使得a变为block::

	.logo_main a { width:110px; height:25px; background-image:url('media/img/theme/logo_main-hover.png') !important;
	}
	.logo_main a { float:left; background:no-repeat left top; }
	.logo_main a:hover, .logo_main a:active, .logo_main a:focus { background-position:left bottom; }

隐藏文字::

	.offset {
		text-indent: -9999px;
		overflow: hidden;
	}

print.css中设置，使得logo在print时不出现，而print图片出现::

	.print { display:block; position:static; left:0; }
	.noprint { display:none !important; }


.pngfix借助js插件实现在ie6下显示png

h1通过padding:20px 0来扩大边界，h2使用position:absolute;right:10px;top:23px;来定位到右边

使用隐藏hr包裹隐藏导航，貌似是为了其他设备使用，然后建立隐藏锚点<h2 class="hidden" id="navigation">Navigation:</h2>通过#navigation来跳转

知识点
=====================

===========	===========
position
===========	===========
absolute	相对于 static 定位以外的第一个父元素进行定位
fixed		相对于浏览器窗口进行定位。
relative	相对于其正常位置进行定位。
static		默认值。没有定位，元素出现在正常的流中（忽略 top, bottom, left, right 或者 z-index 声明）。
===========	===========
