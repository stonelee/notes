.. _vim:

***************
vim
***************

每列后面加+::

	ctrl-V G $ A + Esc退出编辑模式

离开 Vim::

	:qa!<Enter>

检查filetype::

	:set filetype

转换为html格式::

	:TOhtml

record后重复上一次记录的命令::

	@@

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
ctrl-]	帮助文件中跳入
ctrl-t	跳回
=======	=======

查找
=============================

::

	查找	\正则
	强制只搜索小写word	/\Cword
	找到后光标偏移到下面两行的行首	/word/2
	光标偏移到匹配末尾	/word/e
	光标偏移到匹配末尾+1	/word/e+1
	光标偏移到匹配首+1	/word/b+1

记录
=============================

1. qx -> 开始键盘记录（在x缓存中）。（在正常状态）
#. 要记录的“工作”
#. q -> 结束记录。（在正常状态）

@x 使用record

分割窗口
=============================

尽可能扩展窗口::

	CTRL-W _

平均显示多个窗口::

	ctrl+w+= 

打开窗口编辑一个新文件::

	:vnew

命令行中比较两个文件::

	vimdiff main.c~ main.c

vim中将当前文件与其他文件比较::

	:vertical diffsplit main.c~

窗口绑定滚动::

	:set scrollbind

下一处不同::

	]c

反向跳转::

	[c

编译vim
=============================

::

	yum install ncurses-devel
	yum install python-devel
	yum install libgnome-devel
	yum install libgnomeui-devel
	yum install libXt-devel

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

