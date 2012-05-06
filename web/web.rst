.. _web:


***************
web开发综述
***************


cookie,session,auth
=========================

http是无状态的，因此需要采用其他手段保存用户信息

服务端生成cookie发给客户端，然后客户端请求页面时，会将cookie发回服务端，因此可以用于用户识别。但是cookie容易被篡改，被嗅探，而且可能被用户关掉，所以不要用来存储敏感验证数据

session把数据存储在服务端数据库中，通过在cookie中传输sessionID来获取数据

django中session借助cookie实现，而auth是对session的高层封装

学习
=========================

正则
http://blog.csdn.net/lxcnn/article/details/4476746
