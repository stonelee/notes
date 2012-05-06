.. _extjs:


***************
extjs
***************

想法
=============================

按模块划分mvc有利于模块复用,但是Extjs的mvc是整个应用的划分，不利于模块复用。

ExtJS之所以慢在很大程度上是因为需要在客户端解析js生成html，如果能够在服务端解析，生成html并缓存，然后发给客户端，应该能够解决这个问题

总结
=============================

store.findRecord(fieldName, value,null,null,null,true)
最后一个参数为true，否则会模糊查询，返回第一个查到的结果

Ext.define中配置参数中的this指向的是window，因此如果想引用该class的属性，应该在initComponent中使用。

getElConfig使用DomHelper方式来配置控件

* Ext.getCmp(id)	单例时使用
* Ext.container.Container.getComponent(itemId)

ownerCt	得到父Container

======	====
query	所有后代
down	first后代
child	first direct child
======	====

为保证初始化和切换tab时都加载store，tabs中的grid需要同时设置render和show两个事件。
因为tabs render时会触发第一个tab中grid的render事件，但是不会触发show事件；
点击第二个tab时会先后触发其grid的render和show事件；
切换tab时会触发相应grid的show事件

一般grid设置render即可，因为默认不会触发show事件

Ext.extend在原class基础上创建新class,而Ext.override修改原class
