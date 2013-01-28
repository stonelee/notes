.. _svg:

***************
svg
***************

requiredFeatures可以检测浏览器对svg的支持情况::

	<rect class="ok" x="10" y="10" height="25" width="430"
			  requiredFeatures="http://www.w3.org/TR/SVG11/feature#SVG" />

switch进行条件render::

	<switch>
		<!-- If you have set French as one of the language available in your browser then you'll see the word "Français" -->
			<text systemLanguage="fr"
				  text-anchor="middle"
				  x="50" y="25">Français</text>

		<!-- but if you do not have set French and you have set English then you'll see the word "English" -->
			<text systemLanguage="en"
				  text-anchor="middle"
				  x="50" y="25">English</text>

		<!-- and if you have not set French nor English you'll see the word "???" -->
			<text text-anchor="middle"
				  x="50" y="25">???</text>
	</switch>

viewbox相当于对其包裹的元素进行了一次transform::

	<svg width="150px" height="200px" version="1.1"
		 viewBox="0 0 1500 1000" preserveAspectRatio="none"
		 xmlns="http://www.w3.org/2000/svg">

相当于::

	<g transform="scale(0.1 0.2)">

即元素使用viewBox的坐标，但是显示时缩放到svg width，height这个范围内


svg中pointer-events设置element是否接收鼠标事件，实现穿过元素而使得下面的元素接收鼠标事件.
为all时即使fill或stoke为none也可以接收鼠标事件，使得空心矩形也可以通过点击空心被选中。

svg-editor
=============

svgicons默认将svg图形用data URI的方式进行编码，然后作为图标加载。
好处是减少HTTP请求。最大坏处是经过Base64编码字符串很大

* no_img直接加载svg
* 页面不同标签加载同一图像时，使用placement
* resize更改图像大小



ASV
==============

ASV中没有style这种直接赋值的方法，应该使用setAttribute::

  node.setAttribute('style', 'fill:#ccc;');
  //node.style['fill'] = '#ccc';
