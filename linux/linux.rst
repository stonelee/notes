.. _linux:


***************
linux
***************

基本操作
=============================

查看端口号：lsof -i:80

工具
=============================

代码统计: `cloc <http://cloc.sourceforge.net/>`_

fedora启动失败
=============================

启动fedora，提示::

	Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)

更换其他内核可以进入

查看/bin/grub2/grub.cfg, 发现最新内核下少了initrd/boot/initramfs-\*.img

重新生成img::

	$ yum reinstall kernel
