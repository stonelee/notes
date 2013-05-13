.. _regulate:


***************
css规范
***************

顺序
==========

Mozilla method::

  display
  visibility
  float
  clear

  position
  top right bottom left
  z-index

  width min-width max-width
  height min-height max-height
  overflow

  margin margin-top margin-right margin-bottom margin-left
  padding padding-top padding-right padding-bottom padding-left

  border border-top border-right border-bottom border-left
  border-width border-top-width border-right-width border-bottom-width border-left-width
  border-style border-top-style border-right-style border-bottom-style border-left-style
  border-color border-top-color border-right-color border-bottom-color border-left-color

  outline

  list-style

  table-layout
  caption-side
  border-collapse border-spacing
  empty-cells

  font font-family font-size
  line-height
  font-weight
  text-align text-indent text-transform text-decoration
  letter-spacing
  word-spacing
  white-space
  vertical-align
  color

  background background-color background-image background-repeat background-position

  opacity

  cursor

  content
  quotes

Hacks
================

来自豆瓣css规范： https://github.com/kejun/CSS-Code-Guideline

::

  区别属性：

  IE6  _property:value
  IE6/7  *property:value
  IE6/7/8/9  property:value\9
  非IE6  property//:value

  区别规则：

  IE6 * html selector { … }
  IE7 *:first-child+html selector { … }
  非IE6 html>body selector { … }
  firefox only @-moz-document url-prefix() { … }
  saf3+/chrome1+ @media all and (-webkit-min-device-pixel-ratio:0) { … }
  opera only @media all and (-webkit-min-device-pixel-ratio:10000),not all and (-webkit-min-device-pixel-ratio:0) { … }
  iPhone/mobile webkit @media screen and (max-device-width: 480px) { … }
