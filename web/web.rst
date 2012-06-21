.. _web:


***************
web开发
***************

site:stackoverflow.com 

免费域名: http://my.dot.tk/

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

学习
=========================

正则
http://blog.csdn.net/lxcnn/article/details/4476746

设计书籍
http://sachagreif.com/ebook/#!prettyPhoto
http://bootstrappingdesign.com/
http://www.amazon.cn/gp/product/1119998956/ref=as_li_ss_tl?ie=UTF8&linkCode=as2&camp=1789&creative=390957&creativeASIN=1119998956&tag=programming-23

