.. _fedora:


***************
fedora
***************

chrome插件位置::

  ~/.config/google-chrome/Default/Extensions

查看fedora版本::

  cat /etc/issue

安装
---------------

中文输入法：Input Method Selector选择Use IBus，选择Pinyin，改为双拼，不要使用Intelligent Pinyin（不支持lue等）

将Caps Lock变为ctrl键::

  setxkbmap -option ctrl:swapcaps

常用::

  stardict
  flash-plugin
  tomboy

nginx::

  nginx
  配置：ln ～/config/nginx.conf /etc/nginx/nginx.conf

mongodb::

  mongodb-server
  mongodb

版本控制::

  mercurial,tortoisehg
  git
  git-gui

vim::

  vim-enhanced
  ctags
  ack

jslint插件::

  需要先通过yum安装ruby，rubygem-rake
  安装node
  $ rake install
  配置文件config/jslintrc 链接到～/.jslintrc

编译::

  gcc
  gcc-c++

java::

  maven
  mysql
  mysql-server
  mysql-workbench
  启动：$ service mysqld start
  设置密码：mysqladmin -u root password admin
  更改数据库编码：config/mysql/my.cnf 连接到 /etc/my.cnf

安装node，npm，express::

  git clone https://github.com/joyent/node.git
  curl http://npmjs.org/install.sh | sh
  npm install -g express

  编译安装node 0.6.11
  要安装openssl-devel

安装virtualbox
----------------------------

yum install kernel-devel

安装dkms使得内核变动后自动编译

重新编译内核：/etc/init.d/vboxdrv setup

虚拟机中的Gateway即为主机的ip，可以直接访问

配置php环境
--------------------

::

  yum install php

在/var/www/html中创建测试文件info.php::

  <?php
    phpinfo();
  ?>

可以看到测试页面。

::

  yum install php-mysql php-gd php-imap php-ldap php-odbc php-pear php-xml php-xmlrpc php-eaccelerator php-magickwand php-magpierss php-mapserver php-mbstring php-mcrypt php-mhash php-mssql php-shout php-snmp php-soap php-tidy

重启Apache2::

  $ service httpd restart

非root权限安装nginx
------------------------

编译安装::

  ./configure --prefix=/home/vboxadmin/lxd/bin/nginx  --without-http_rewrite_module --without-http_gzip_module
  make
  make install

conf/nginx.conf将端口改为8090（1-1024需要管理员权限）

运行 sbin/nginx

停止 sbin/nginx -s stop

Fedora 10里将普通用户添加到sudo组
----------------------------------

1. 在终端输入su -
#. 输入密码， 这样就切换到root了
#. 输入visudo
#. 找到 root ALL=(ALL) ALL 在这一行下边按a键进入编辑模式，然后输入： yourname ALL=(ALL) ALL,然后按esc退出
#. 按 :wq 键保存退出
#. 输入exit退出root权限
#. 测试，在当前用户下，输入sudo whoami

如果一切正常，命令会返回 “root” 这个字。


fedora启动失败
-------------------

启动fedora，提示::

  Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)

更换其他内核可以进入

查看/bin/grub2/grub.cfg, 发现最新内核下少了initrd/boot/initramfs-\*.img

重新生成img::

  $ yum reinstall kernel

fedora启动时显示启动信息
----------------------------------

1. 编辑/etc/default/grub， 去掉GRUB_CMDLINE_LINUX中quiet和rhgb
#. /sbin/grub2-mkconfig -o /boot/grub2/grub.cfg
#. 查看/boot/grub2/grub.cfg，启动配置中已经没有了quiet，rhgb选项。

给ibus-pinyin加上搜狗细胞词库
----------------------------------

下载:https://code.google.com/p/hslinuxextra/downloads/detail?name=sougou-phrases-full.7z&can=2&q=

解压后android.db文件就是ibus-pinyin的词库

打开/usr/share/ibus-pinyin/db，将android.db改名覆盖

重启ibus激活


访问远程共享文件
-------------------------

* 文件夹管理器中File-Connect to Server
* server填远程机器的ip，type选Windows share，填入用户名，密码即可

window访问远程共享文件

开始-搜索中输入\\10.10.22.110，然后就可以打开该机器的共享文件夹

