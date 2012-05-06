.. _architecture:


***************
系统架构
***************

豆瓣
=============================


Web server上划分为动态html和静态图片,做不同的调优

动态内容使用nginx和lighttpd的混合，nginx做负载的平衡，lighttpd通过SCGi与application server相连，application server基于quixote框架
静态部分用nginx

日记贴图用mogile FS ，这是一个分布式的文件系统，同时可以做备份，保持高可用性，可以提高很大的IO。
使用Memcached作为cache，可以提供分布式内存cache，豆瓣自己开发了client端访问多台机器的内存cache

搜索请求用搜索引擎。Xapian是一个C++写的开源的搜索引擎，我们通过Web service去访问它。

数据库根据应用划分，使用MySQL，一个master ，一个 slave，还有一个slave,一方面作为备份，一方面用作数据挖掘，因为不能对线上的数据做直接操作。

View模版使用mako，容易维护，自己做了速度优化，并反馈回社区
