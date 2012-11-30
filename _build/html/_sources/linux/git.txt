.. _git:


***************
版本控制
***************


git
=============================

升级子模块::

  $ git submodule update --init --recursive

RhodeCode中推送已经存在的库::

  $ git push http://stonelee@10.10.22.86:1080/parseCSV master

如果报错::

  RhodeCode error: RPC failed; result=22, HTTP code = 502
  fatal: The remote end hung up unexpectedly

应该设置::

  $ git config http.postBuffer 524288000

如果做了修改或删除，想回到版本控制的状态::

	git checkout .

提交::

	git commit -a -m 'Validation!'

如果Fork别人的项目或者多人合作项目，最好每人都拥有一个独立分支，然后由项目维护人合并。

如何建立自己的分支
----------------------

* git branch yourbranch 创建分支
* git checkout yourbranch 切换到yourbranch
* 开发yourbranch分支，然后开发之后与master分支合并
* git checkout master
* git merge yourbranch
* git branch -d yourbranch 合并完后删除local

如何将牛人的远程分支更新到自己的本地分支？
-------------------------------------------

* git remote 查看当前项目下远程
* 增加新的分支链接，例如 git remote add niuren giturl…
* 获取牛人的远程更新 git fetch niuren
* 将牛人的远程更新合并到本地分支 git merge niuren/master


避免push时填入密码，通过ssh
---------------------------------

::

  git remote set-url origin git@github.com:user/repo.git

git pages
=============================

创建两个branch。在master中开发，稳定版本merge到gh-pages中。参见：https://github.com/aralejs/aralejs.github.com

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
