.. _vim:

***************
vim
***************

:syntax on 开始语法着色

使用session保存当前环境

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

删除空白行::

  :g/^\s*$/d

跳转

::

  e   下一个单词末
  w   下一个单词开始
  b   上一个单词开始
  单词仅仅由字母数字-_组成，跳转使用小写
  单词包含除空格、tab之外的字符，跳转使用大写

  %   括号跳转

  ma    标识本文件缓冲区位置a
  'a    跳到本文件位置a
  mA    标识全局缓冲区位置A
  'A    跳到其他文件位置A
  ''    跳回上一个位置

  ctrl-o  跳回
  ctrl-i  跳到
  ctrl-]  帮助文件中跳入
  ctrl-t  跳回

  {       段落前或者前面的空行
  }       段落后或者后面的空行

  类似在栈中暂存更改位置
  g,      返回刚刚修改过的地方（没什么用）
  g;      循环跳到每一个更改处

  vim默认提供c的结构跳转，另外还能进行括号和花括号的跳转
  借助matchit插件可以在编程语句内部使用%进行语法跳转，

  gd (Goto Declaration) 跳转到初次定义
  gj                    行内移动
  ctrl-w j              window间跳转

查找
=============================

::

  查找  \正则
  强制只搜索小写word  /\Cword
  找到后光标偏移到下面两行的行首  /word/2
  光标偏移到匹配末尾  /word/e
  光标偏移到匹配末尾+1  /word/e+1
  光标偏移到匹配首+1  /word/b+1

  set incsearch 可以在使用/搜索时实时将鼠标自动移到目标位置
  / 向后搜索
  ? 向前搜索


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

Terminal中报错::

  CSApprox needs gui support - not loading.
    See :help |csapprox-+gui| for possible workarounds.

需要安装GUI版本的vim::

  yum install vim-X11
  cp /usr/bin/gvim /usr/bin/vim

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

插件冲突与问题
==================

1.ack.vim与jslint.vim有冲突。
jslint会覆盖ack的所使用的quickfix窗口，需要:cnew来查看结果

2. snip跟自动提示冲突。
在预定义变量位置进行编辑时，如果出现自动提示，snip模板中定义的该变量在其他位置的引用均不跟着一起变化
