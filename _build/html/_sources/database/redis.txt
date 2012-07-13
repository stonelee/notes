.. _redis:


***************
redis
***************

基本命令
=============================

官方网站
http://redis.io/download

打开服务端::

	$ src/redis-server

客户端::

	$ src/redis-cli

在线命令学习
=============================

http://try.redis-db.com/

key-value

================   ================
目的               操作
================   ================
设置key value      SET server:name "fido" （SETNX -- "SET if Not eXists"）
获取value          GET server:name => "fido"
删除key            DEL connections
原子操作加1        INCR connections => 1
超过120s会删除     EXPIRE resource:lock 120
监测还保留多久     TTL resource:lock => 113 （-1表示不会过期）（重新SET会reset过期时间）
================   ================

list（ordered values）

================   ================
目的               操作
================   ================
加到末尾           RPUSH friends "Tom"
加到开始           LPUSH friends "Sam"
得到list           LRANGE friends 0 1 => ["Sam","Tom"] （0 based，第二个参数为-1表示取剩下的所有）
取个数             LLEN friends => 3
删第1元素并返回    LPOP friends => "Sam"
删最后元素并返回   RPOP friends => "Bob"
================   ================

set（没有order，不重复）

================   ================
目的               操作
================   ================
添加               SADD superpowers "flight"
删除               SREM superpowers "reflexes"
检查是否在set中    SISMEMBER superpowers "flight" => true
得到set            SMEMBERS superpowers => ["flight","x-ray vision"]
并集               SUNION superpowers birdpowers => ["flight","x-ray vision","pecking"]
================   ================

sorted set（元素有权值的set）

================   ================
目的               操作
================   ================
添(score,value)    ZADD hackers 1940 "Alan Kay"
得到               ZRANGE hackers 2 4 => ["Alan Kay","Richard Stallman","Yukihiro Matsumoto"]
================   ================

redis-tutorial
====================================================

http://simonwillison.net/static/2010/redis-tutorial/

* key命名 obj-type:id:field => (user:23:username)
* TYPE => the type of a Redis key(string, list, set, zset, hash or none)
* ends with an NX => Not Exists

Redis can work as a cache (similar to memcached) by using the EXPIRE and EXPIREAT

