.. _web:


***************
web开发
***************

Fiddler:IE下http数据流分析工具
http://www.fiddler2.com/fiddler2/

site:stackoverflow.com 

免费域名: http://my.dot.tk/

iframes性能问题
=========================

http://9.douban.com/site/entry/259738987/

1. iframes的创建比其它包括scripts和css的 DOM 元素的创建慢了 1-2 个数量级。

#. Iframes 阻塞页面加载onload 事件

	onload 事件触发使浏览器的 “忙” 指示器停止，告诉用户当前网页已经加载完毕。当 onload 事件加载延迟后，它给用户的感觉就是这个网页非常慢。

	window 的 onload 事件需要在所有 iframe 加载完毕后(包含里面的元素)才会触发。在 Safari 和 Chrome 里，通过 JavaScript 动态设置 iframe 的 SRC 可以避免这种阻塞情况。

#. 唯一的连接池

	浏览器只能开少量的连接到web服务器。比较老的浏览器，包含 Internet Explorer 6 & 7 和 Firefox 2，只能对一个域名(hostname)同时打开两个连接。Safari 3+ 和 Opera 9+ 可同时对一个域名打开 4 个连接，Chrome 1+, IE 8 以及 Firefox 3 可以同时打开 6 个。

	绝大部分浏览器，主页面和其中的 iframe 是共享这些连接的。这意味着 iframe 在加载资源时可能用光了所有的可用连接，从而阻塞了主页面资源的加载。

	如果 iframe 中的内容比主页面的内容更重要，这当然是很好的。

	但通常情况下，iframe 里的内容是没有主页面的内容重要的。这时 iframe 中用光了可用的连接就是不值得的了。一种解决办法是，在主页面上重要的元素加载完毕后，再动态设置 iframe 的 SRC。

cookie,session,auth
=========================

http是无状态的，因此需要采用其他手段保存用户信息

服务端生成cookie发给客户端，然后客户端请求页面时，会将cookie发回服务端，因此可以用于用户识别。但是cookie容易被篡改，被嗅探，而且可能被用户关掉，所以不要用来存储敏感验证数据

session把数据存储在服务端数据库中，通过在cookie中传输sessionID来获取数据

django中session借助cookie实现，而auth是对session的高层封装

多进程与多线程
=========================

Windows下创建进程的时间开销比linux下大接近100倍，因此鼓励多线程，但是要注意资源争抢与同步方面的问题。 
Linux鼓励多进程，但是要考虑进程间通讯的方法。

大量创建进程的典型例子有两个，一个是 gnu autotools 工具链在 Windows 下编译速度很慢。另一个是服务器，某些服务器框架依靠大量创建进程来干活，甚至是对每个用户请求就创建一个进程，这些服务器在 Windows 下运行的效率就会很差。

svg
=========================

svg的优势在于手机，浏览器可以使用同一套图片，缩放不失真

引用方式包括

* img src=
* object data=	可以解析脚本

svg与canvas的区别

* svg类似于DOM
* canvas类似于GDI	可以精确到像素级

svg+canvas组合使用

* svg通过img src指定，提供图片加载，在onLoad事件中context.drawImage
* canvas渲染特效，如燃烧，粒子

html5手机端开发
=========================

使用native可以借助内置特性，例如html跳转使用native而不是history，可以使用native动画

海量访问笔记
=========================

http://www.cnblogs.com/wrmfw/archive/2012/01/21/2328534.html

打开淘宝首页，浏览器查询DNS服务器：域名转换为ip地址

DNS解析域名时负载均衡到不同的ip地址，将访问分配到不同的入口

生成淘宝首页页面的服务器有很多台，通过LVS（Linux Virtual Server）来分配

浏览器在同一个域名下并发加载的资源数量是有限制的，因此将资源分布在多个域名下，变相的绕过浏览器的这个限制，同时也为CDN工作做准备

CDN（Content Delivery Network，内容分发网络）保证访问的资源(这里主要指js、css、图片等)所处的位置是最近的CDN节点，避免不同地区不同网络(电信、联通等)之间互访，可以分散流量。

CDN节点会有中内容分发与同步的问题，淘宝开发了分布式文件系统TFS(taobao file system)

搜索使用分词，把中文的汉字序列切分成有意义的词，就是中文分词，也称为切词

进行分词之后，还需要根据你输入的搜索词进行你的购物意图分析。用户进行搜索时常常有如下几类意图：（1）浏览型：没有明确的购物对象和意图，边看边买，用户比较随意和感性。Query例如：”2010年10大香水排行”，”2010年流行毛衣”， “zippo有多少种类？”；（2）查询型：有一定的购物意图，体现在对属性的要求上。Query例如：”适合老人用的手机”，”500元 手表”；（3）对比型：已经缩小了购物意图，具体到了某几个产品。Query例如：”诺基亚E71 E63″，”akg k450 px200″；（4）确定型：已经做了基本决定，重点考察某个对象。Query例如：”诺基亚N97″，”IBM T60″。通过对你的购物意图的分析，主搜索会呈现出完全不同的结果来。

数据保存和快速调用使用Tair，淘宝自行研发的分布式KV存储方案

记录用户访问行为，用于后续的业务逻辑和数据分析。为了快速及时传输同步这些日志数据，淘宝研发了TimeTunnel，用于进行实时的数据传输，交给后端系统进行计算报表等操作。

如此巨大的数据量经过淘宝系统1:120的极限压缩存储在淘宝的数据仓库中。并且通过一个叫做云梯的，由2000多台服务器组成的超大规模数据系统不断的进行分析和挖掘

* PV（Page View）：页面访问，按访问页面数计算
* UV（Unique Visitor）：用户访问，按用户数计算

学习
=========================

正则
http://blog.csdn.net/lxcnn/article/details/4476746

设计书籍
http://sachagreif.com/ebook/#!prettyPhoto
http://bootstrappingdesign.com/
http://www.amazon.cn/gp/product/1119998956/ref=as_li_ss_tl?ie=UTF8&linkCode=as2&camp=1789&creative=390957&creativeASIN=1119998956&tag=programming-23

