.. _extjs:


***************
extjs
***************

Ext.DomHelper.append貌似不能正常添加bgsound，使用dom语句生成在IE各版本中表现一致

基本API
=============================

* Ext.getCmp(id)	单例时使用
* Ext.container.Container.getComponent(itemId)

=======	=========
getCmp	得到component
get		得到element
=======	=========

ownerCt	得到父Container

======	====
query	所有后代
down	first后代
child	first direct child
======	====

===========================	=====
Ext.util.HashMap			无顺序
Ext.util.MixedCollection	有顺序
===========================	=====

Ext.iterate可以同时迭代object和array

===========	=========
Ext.merge()	递归合并（内部object也合并），后面的会把前面的覆盖
Ext.apply()	不递归
===========	=========

::

	store.loadPage(1,{params:{query:'something'}})
	store.clearFilter()
	store.filter('name','some')

store.findRecord(fieldName, value,null,null,null,true)
最后一个参数为true，否则会模糊查询，返回第一个查到的结果

Ext.extend在原class基础上创建新class,而Ext.override修改原class

技巧
=============================

initComponent中使用this.initialConfig来获取实例的配置参数

Ext.define中配置参数中的this指向的是window，因此如果想引用该class的属性，应该在initComponent中使用。

getElConfig使用DomHelper方式来配置控件

Ext.form.Panel通过getForm()得到Ext.form.Basic（辅助类）的实例，从而完成验证，提交，加载等功能。

loadRecord调用的是field.setValue

数组用，隔开，字符直接显示::

	me.displayTpl = Ext.create('Ext.XTemplate',
		'<tpl for=".">' +
			'{[typeof values === "string" ?  values : values["' + me.displayField + '"]]}' +
			'<tpl if="xindex < xcount">' + me.delimiter + '</tpl>' +
		'</tpl>'
	);

函数正常运行，返回true，有异常返回false

store
-------------------------

为保证初始化和切换tab时都加载store，tabs中的grid需要同时设置render和show两个事件。
因为tabs render时会触发第一个tab中grid的render事件，但是不会触发show事件；
点击第二个tab时会先后触发其grid的render和show事件；
切换tab时会触发相应grid的show事件

一般grid设置render即可，因为默认不会触发show事件

配合pagingtoolbar的store，都要通过getProxy().extraParams的方式更改参数

store跟控件是绑定的，如果同一个页面的多个控件关联同一个store，会出现状态同步的现象，解决方法是新创建一个store

TreeStore
-------------------------

TreeStore必须要使用model，model和TreeStore都要在controller中引用，

不能使用名为“Trees”的store和名为Tree的model

TreeStore当有节点expand时自动加载数据，因此如果在TreeStore的子类中设置root:{expanded:true}时会在create该store时加载数据,否则会在Tree.Panel的load事件中加载。

combobox
-------------------------

如果设置::

	displayField:'name';valueField:'id';name:'name'
	
对于::

	record=Ext.create('KJExt.model.Student',{name:2})

::

	this.up('form').getForm().loadRecord(record)

只会显示id，但是下拉列表中会自动高亮选择该项

改进：

在form的render事件中先load该store，则会显示name，但是第一次点击下拉列表会自动收缩，以后就没事了。

注意：

如果在按钮点击事件中store.load，会在重新点击按钮，然后点击下拉列表后报错

推荐做法：

如果赋值为object，可以正确显示，但是下拉列表不会自动高亮::

	combobox设置：
	{
		xtype: 'combobox',
		store: 'Students',
		valueField: 'id',
		displayField: 'name',
		name: 'student'
	}
	赋值方法：
	Ext.define('Record', {
		extend: 'Ext.data.Model',
		fields: ['id', 'student']
	});
	var myStore = Ext.create('Ext.data.Store', {
		model: 'Record',
		data: [{
			id: 1,
			student: {
				id: 2,
				name: 'jerry'
			}
		}]
	});
	var record = myStore.getRange()[0];
	this.up('form').getForm().loadRecord(record);


examples
=============================

4.1.0-kitchensink
-------------------------

使用neptune样式，适合触摸屏使用

Viewport中layout:'border'中如果设置左右两边,可以直接设置::

	region:'center',
	layout:{
		type:'hbox',
		align:'stretch'
	},
	items:[]

hbox中的控件通过flex设置按比例自动扩展

hbox中设置pack:'center'会使得items横向居中显示，align:'stretch'会使得纵向达到最大

overflowY:'auto'单独设置y轴滚动条

如果要设计模块统一风格，可以使用ui，如在toolbar的子类中设置ui:'sencha',会生成class=“x-toolbar-sencha”
单独设置控件class，使用cls:'x-logo'

通过defaults来设置items中的默认值，可以嵌套

{}的默认xtype是‘panel'

form默认layout为anchor，可以默认设置::

	defaultType:'textfield',
	defaults:{anchor:'100%'}

通过location.hash来保存页面地址，进而通过url设置页面::

	在左侧树的select事件中:
	location.hash='someid';
	document.title=document.title.split(' - ')[0]+' - '+title

	在左侧树的afterrender事件中:
	name=location.hash.substring(1);
	record=treepanel.view.store.find(key,name)
	treepanel.view.select(record);

新的代码组织方式::

	(function(){
		var toolbarItems = [];
		Ext.define();
	})();

这种方式可以将某些配置项抽象出来，使得定义模块时依然可以直接配置

simple-tasks
-------------------------

bodyStyle:设置body的style属性

grid's column的weight:100，如果设某个dockedItem的weight:101,则排在column的下面，默认toolbar为0，所以排在最上面

extjs使用规范
=============================

为了顺利完成打包工作：

* js里面统一使用单引号，尤其是在requires中
* view中如果要通过xtype方式引用其他view，必须在requires中引入该文件
* controller中的views只应该包含没有被任何view文件require的view

想法
=============================

按模块划分mvc有利于模块复用,但是Extjs的mvc是整个应用的划分，不利于模块复用。

ExtJS之所以慢在很大程度上是因为需要在客户端解析js生成html，如果能够在服务端解析，生成html并缓存，然后发给客户端，应该能够解决这个问题

更改css
================

::

	gem install sass -v 3.1.1
	gem install compass

查看版本号::

	compass -v
	sass -v

目录结构::

	appname
	--app/
	--extjs/
	--resources/
	  --css/
	  --images/
	  --sass/
	--app.js
	--index.html


更改css模板：
appname/resources/sass/my-ext-theme.scss

可控制的变量：
appname/extjs/resources/themes/stylesheets/ext4/default/variables/

编译css:
在appname/resources/sass中运行compass compile

优化
================

貌似Ext的底层封装实现中，会在用户绑定的事件中阻塞整个css的渲染，需要等待所有css计算完成后再统一进行。这在效率上真是做到了我能想到的极致！只是如果想在其中加入自己的css动态实现时难免会掉到坑里

关于Extjs项目打开页面慢的问题

我们现在要解决的是渲染慢问题，因为局域网基本不需要考虑加载问题。

经过分析，现在渲染慢的原因在代码层面主要有：

* 业务划分不合理，很多组件显示在一个页面上整体显示
* 有些代码确实不规范，其中最影响性能的就是面板多次嵌套，再就是使用了组件树中功能多的组件而没有优先选用适合自己需要的简单组件

网上那些减少渲染问题的手段，比如避免使用iframe，合并压缩，延迟创建组件我们从一开始就已经这么用了。
委托模式我们还没有使用，不过这个跟页面打开的渲染速度无关

解决方案按难度排列如下：

* 最立竿见影的方法就是在页面上加个提示，提示用户换浏览器
* 换浏览器之后还是有些页面比较慢，可以在上面加loading提示，在视觉上减少加载时间
* view层的页面重构，将慢的页面嵌套看能不能精简，这个实际上跟业务有点关系，页面显示效果恐怕就会变了
* 业务层面拆分，将本来一页显示的内容变为多页，这得修改该模块的架构，包括controller，view等，修改量更大
* 代码逐句调优，比如说缓存select，工作量不小，效果不大。
* 如果还是慢只能将该部分页面由ExtJS换为jquery自己模拟实现，难度更大。

优化记录
----------

将layout由hbox方式改为table方式，效率差不多

使用fieldset隐藏不需要马上渲染的组件，可以有效减少加载时间::

  {xtype : 'fieldset',collapsible : true,collapsed: true}


