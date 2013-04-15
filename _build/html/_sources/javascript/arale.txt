.. _arale:

***************
arale
***************

class
-------------

查看类的继承关系::

  seajs.log(dog, 'dir')

另外附加prototype方法，会覆盖同名方法::

  Implements: [Flyable, Talkable]

或者::

  Dog.implement({
    talk: function() {
      return 'I am ' + this.name
    }
  })

设置静态属性::

  Statics: {
    COLOR: 'red'
  },

或者::

  Animal.LEGS = 4

为继承自A的类的静态属性设置白名单，防止继承多余的父类的静态属性::

  A.StaticsWhiteList = ['a']

如果不设置此属性则不使用白名单过滤

设置初始值，如new Dog('Jack')::

  initialize: function(name) {}

或者::

  function Dog(name)

调用父类方法::

  Dog.superclass.initialize()

events
------------

监听的事件保存在__events中，__events为对象字面量，key为事件名称（all意味着响应所有事件,在on中指定），
值为一维数组，内容为每个响应事件的回调和上下文，两两依次排列

base
----------------

混入了Events，Aspect， Attribute中的方法

destroy:删除绑定的事件，删除方法

attribute配置项::

  value: '#test',
  readOnly: true
  getter: function() {
    return this.get('x') + this.get('y');
  },
  setter: function(val) {
    this.set('x', val[0]);
    this.set('y', val[1]);
  }

_onChangeX 方法会自动注册到 change:x 事件::

  _onChangeColor: function(val, prev, key) {
    this.element.css('backgroundColor', val);
  }

例子::

  var A = Base.extend({
    attrs: {
      color: '#fff',
      size: {
        width: 100,
        height: 100
      }
    },
    show: function() {
      // Do some cool stuff
      this.trigger('show');
    }
  });

在配置中响应事件::

  var a = new A({
    color: '#f00',
    size: {
      width: 200
    },
    onShow: function() {
      counter++;
    },
    afterShow: function() {
      counter++;
    },
    beforeShow: function() {
      counter++;
    },
    onChangeColor: function() {
      counter++;
    }
  });

额外指定事件::

  a.on('change:x', function(val, prev, key) {

aspect::

  a.before('xxx', function(n, m) {

propsInAttrs使得位于attrs之外的配置也可以通过getter,setter调用,同时也保存在attrs中,
调用也非常方便::

  var T = Base.extend({
    attrs:{
      foo:'foo'
    },
    model: {
      getter: function(val) {
        return {
          a: 1,
          v: val
        };
      }
    },
    propsInAttrs: ['model']
  });

  var t = new T({
    foo:'abc',
    model:'my',
  });

  console.log(t.get('foo'));//abc
  console.log(t.model);//{a:1,v:"my"}
  console.log(t.get('model'));//{a:1,v:"my"}

Attribute
==============

initAttrs将用户配置与attrs以及继承得到的attrs进行合并，将实例方法_onChangeAttr注册为change:attr事件的响应，
将用户配置中的on/before/afterXxx注册为事件响应

get获取attr的值，可通过getter

set设置attr的值，可通过setter，默认会触发change:x事件，
如果设置参数slient:true, 此时不会自动触发change:x事件, 会设置__changedAttrs.
默认新旧值merge，如果设置参数override:true, 则直接覆盖

change手工触发__changedAttrs的change事件

用户调用可配置内容包括：attrs,on/before/afterXxx,propsInAttrs

Aspect
============

貌似比较鸡肋

before在指定方法前执行任务，参数与指定方法参数相同，不能通过return false停止向下执行

after在指定方法后执行任务，参数为指定方法的返回值，貌似对于异步回调依然木办法

可以同时指定多个方法，用空格隔开

widget
--------------

View 层的管理。

* 描述状态的 attributes 和 properties
* 描述行为的 events和 methods

config 中的这些键值会直接添加到实例上，转换成 properties::

  propsInAttrs: ['element', 'template', 'model', 'events']

initialize初始化方法，确定组件创建时的基本流程::

  初始化 attrs --》 初始化 props --》 初始化 events --》 子类的初始化

  // 初始化 attrs，包括用户配置和data-*合并默认属性
  var dataAttrsConfig = this._parseDataAttrsConfig(config)
  this.initAttrs(config, dataAttrsConfig)

  // 初始化 props
  this.parseElement()//构建element，如果没有配置就从template构建
  this.initProps()//供子类覆盖

  // 初始化 events
  this.delegateEvents()

  // 子类自定义的初始化
  this.setup()//供子类覆盖

  // 保存实例信息,会在节点上标记data-widget-cid,让element与Widget实例建立关联
  this._stamp()

events通过this.delegateEvents()使用jquery的on方法进行事件绑定，事件都有命名空间.delegate-events-cid以方便删除，select可以使用{{}}语法指定attrs中的属性

render会当属性xx不为空值时自动调用_onRenderXX(val, prev, key)，并将_onRenderXX绑定到change事件，默认绑定了属性id，style，className，parentNode

Widget.query(select)获取节点对应的Widget实例

Widget.StaticsWhiteList = ['autoRender']指明Widget子类的静态方法只有autoRender

Widget静态方法还包括query，autoRenderAll

在标签里使用data-\*进行配置跟实例化时指定该element传入配置效果是一致的

父类继承时attrs中属性，以及model，events会混合，一般的prototype中的object会覆盖

templatable
============

默认的widget只是简单的从模板构建element,这个组件通过覆盖parseElementFromTemplate方法提供了handlebars模板，并提供局部渲染功能。

混入后, template配置模板，model配置模板变量（也可以用toJSON），templateHelpers配置自定义模板逻辑，由模板自动生成element（jquery对象）

render将widget渲染到页面上

renderPartial渲染部分页面,参数为选择器

为了在局部渲染时可以从内部保存的jquery对象中找到正确的区域，
为避免标签意外关闭，在保存该内部jquery对象时,将{{xx}}转换为<!--{{xx}}-->，
为防止额外加载数据，将src和href替换

daparser
============

提供方法parseElement,解析标签里的data-\*属性。值可以为[],{}，默认会按照json进行转化，并处理为各种易用的类型。第二个参数如果设为true则不进行任何转化

标签里的data-\*会在现代浏览器中存储在元素的dataset中，并可以很方便的进行修改

最好都使用小写, data-some-key会转为someKey

auto-render
============

autoRender，如果子类需要提供更多参数，可以覆盖之

一般使用autoRenderAll()来自动渲染控件。原理是通过data-widget指定模块，然后使用seajs.use分别调用，然后通过向autoRender传入配置 {element: element, renderType: 'auto'}，模块实例化后render

* 全局关闭方法：document.body上设置data-api="off"，然后单个开启：element上设置data-api="on"
* 关闭单个：element上设置data-api="off"

overlay
----------

可以在window.resize时自动定位.

_blurHide设置document.click时元素blur自动hide

fixed
----------

实现跟随滚动的效果，可以设置marginTop，当超出该值时才fixed

实现原理是在ie6下监听scroll事件,然后设置::

  position: 'absolute',
  top: marginTop + doc.scrollTop()

messender
------------

iframe通信

优先使用postMessge.IE中同域使用自定义事件，跨域使用两个隐藏iframe，通过改变其name实现通信

继承结构图
-----------

.. image:: aralejs.png

seajs
--------------

seajs.find('widget')参数为正则查询,返回结果为匹配数组。如果想精确匹配，可以精确指定使用widget.js
