.. _git:


***************
版本控制
***************


git
=============================

github更新子模块::

	$ git submodule init
	$ git submodule update

RhodeCode中推送已经存在的库::

	git push http://stonelee@10.10.22.86:1080/parseCSV master

如果做了修改或删除，想回到版本控制的状态::

	git checkout .

提交::

	git commit -a -m 'Validation!'


hg
=============================

使用本地ignore
----------------

.hg/hgrc中添加::

	[ui]
	ignore = /path/to/repo/.hg/hgignore

然后在.hg/hgignore中列出本地存在但不提交的代码

查看自己提交的log
---------------------

::

	$ hg log -u stonelee --template '{date|isodate} {desc}\n'|more

bitbucket
---------------------

1. 将~/.ssh/id_rsa.pub添加到网站SSH keys中

#. 修改.hg/hgrc文件::

	[paths]
	bitbucket = https://istonelee@bitbucket.org/hsialee/ciis

	[hostfingerprints]
	bitbucket.org = 24:9c:45:8b:9c:aa:ba:55:4e:01:6d:58:ff:e4:28:7d:2a:14:ae:3b

#. TortorseHg中View-Synchronize，选择相应的url进行操作
