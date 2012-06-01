.. _jquery:

***************
jquery
***************

jquery1.7.2中如果在setInterval中循环getJSON同一个地址时，chrome不会显示发送xhr请求，但是firefox中会显示。jquery1.4.2没有这个问题

$.extend可以merge objects，第一个参数True递归merge

防止修改defaults参数::

	var settings = $.extend({}, defaults, options);
