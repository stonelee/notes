.. _hg:


***************
hg
***************

使用本地ignore
=============================

.hg/hgrc中添加::

	[ui]
	ignore = /path/to/repo/.hg/hgignore

然后在.hg/hgignore中列出本地存在但不提交的代码

查看自己提交的log
=============================

::

	$ hg log -u stonelee --template '{date|isodate} {desc}\n'|more
