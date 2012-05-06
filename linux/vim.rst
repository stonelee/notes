.. _vim:


***************
vim
***************

跳转
=============================

=======	=======
命令		功能
=======	=======
e		下一个单词末
w		下一个单词开始
b		上一个单词开始	
%		括号跳转
ma		标识本文件缓冲区位置a
'a		跳到本文件位置a
mA		标识全局缓冲区位置A
'A		跳到其他文件位置A
''		跳回上一个位置
ctrl-o	跳回
ctrl-i	跳到
=======	=======

js taglist
=============================

http://discontinuously.com/2011/03/vim-support-javascript-taglist-plus/

1.生成代码分析
--------------------------

jsctags: https://github.com/mozilla/doctorjs

clone子模块::

	$ git clone --recursive https://github.com/mozilla/doctorjs.git
	$ make install

但是报错.

引入其他人的pull request::

	$ git remote add require https://github.com/zmmbreeze/doctorjs.git
	$ git fetch require
	$ git merge require/master 

~/.profile中添加::

	export NODE_PATH=/usr/local/lib/jsctags/:$NODE_PATH

然后::

	$ source ~/.profile 

2.安装vim插件 
--------------------------

https://github.com/int3/vim-taglist-plus

3.使用
--------------------------

::

	:TlistToggle

