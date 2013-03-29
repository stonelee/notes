.. _git:


***************
版本控制
***************

git
=============================

避免push时填入密码，通过ssh::

  git remote set-url origin git@github.com:user/repo.git

使用代理::

  git config --global http.proxy http://127.0.0.1:8087

升级子模块::

  git submodule update --init --recursive

如果做了修改或删除，想回到版本控制的状态::

  git checkout .

提交::

  git commit -a -m 'Validation!'

添加远程仓库::

  git remote add office http://stonelee:mima@10.10.22.86:1080/raphael

提交::

  git push office

如果Fork别人的项目或者多人合作项目，最好每人都拥有一个独立分支，然后由项目维护人合并。

RhodeCode
--------------

RhodeCode中推送已经存在的库::

  $ git push http://stonelee@10.10.22.86:1080/parseCSV master

如果报错::

  RhodeCode error: RPC failed; result=22, HTTP code = 502
  fatal: The remote end hung up unexpectedly

应该设置::

  $ git config http.postBuffer 524288000


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


如何建立远程库进行管理
------------------------------

远程机器建立空的库::

  git clone --bare raphael.git

本地设置远程访问路径::

  git remote add centos ssh://stonelee@10.10.22.82/home/stonelee/raphael

推送::

  git push centos svg

其他人拉取::

  git clone ssh://stonelee@10.10.22.82/home/stonelee/raphael

切换到svg分支::

  git checkout svg

删除错误提交的commit
-----------------------

起因: 不小新把记录了公司服务器IP,账号,密码的文件提交到了git

方法::

  git reset --hard <commit_id>
  git push origin HEAD --force

其他::

  根据–soft –mixed –hard，会对working tree和index和HEAD进行重置:
  git reset –mixed：此为默认方式，不带任何参数的git reset，即时这种方式，它回退到某个版本，只保留源码，回退commit和index信息
  git reset –soft：回退到某个版本，只回退了commit的信息，不会恢复到index file一级。如果还要提交，直接commit即可
  git reset –hard：彻底回退到某个版本，本地的源码也会变为上一个版本的内容

  HEAD 最近一个提交
  HEAD^ 上一次
  <commit_id>  每次commit的SHA1值. 可以用git log 看到,也可以在页面上commit标签页里找到.

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

将~/.ssh/id_rsa.pub添加到网站SSH keys中

修改.hg/hgrc文件::

  [paths]
  bitbucket = https://istonelee@bitbucket.org/hsialee/ciis

  [hostfingerprints]
  bitbucket.org = 24:9c:45:8b:9c:aa:ba:55:4e:01:6d:58:ff:e4:28:7d:2a:14:ae:3b

TortorseHg中View-Synchronize，选择相应的url进行操作

Git常用操作命令
-----------------

http://rongjih.blog.163.com/blog/static/335744612010112562833316/

远程仓库相关命令::

  检出仓库：$ git clone git://github.com/jquery/jquery.git
  查看远程仓库：$ git remote -v
  添加远程仓库：$ git remote add [name] [url]
  删除远程仓库：$ git remote rm [name]
  修改远程仓库：$ git remote set-url --push [name] [newUrl]
  拉取远程仓库：$ git pull [remoteName] [localBranchName]
  推送远程仓库：$ git push [remoteName] [localBranchName]

  * 如果想把本地的某个分支test提交到远程仓库，并作为远程仓库的master分支，或者作为另外一个名叫test的分支，如下：
  $ git push origin test:master         // 提交本地test分支作为远程的master分支
  $ git push origin test:test              // 提交本地test分支作为远程的test分支

分支(branch)操作相关命令::

  查看本地分支：$ git branch
  查看远程分支：$ git branch -r （如果还是看不到就先 git fetch origin 先）
  创建本地分支：$ git branch [name] ----注意新分支创建后不会自动切换为当前分支
  切换分支：$ git checkout [name]
  创建新分支并立即切换到新分支：$ git checkout -b [name]
  直接检出远程分支：$ git checkout -b [name] [remoteName] (如：git checkout -b myNewBranch origin/dragon)
  删除分支：$ git branch -d [name] ---- -d选项只能删除已经参与了合并的分支，对于未有合并的分支是无法删除的。如果想强制删除一个分支，可以使用-D选项
  合并分支：$ git merge [name] ----将名称为[name]的分支与当前分支合并
  合并最后的2个提交：$ git rebase -i HEAD~2 ---- 数字2按需修改即可（如果需提交到远端$ git push -f origin master 慎用！）
  创建远程分支(本地分支push到远程)：$ git push origin [name]
  删除远程分支：$ git push origin :heads/[name] 或 $ git push origin :[name] 

  * 创建空的分支：(执行命令之前记得先提交你当前分支的修改，否则会被强制删干净没得后悔)
  $ git symbolic-ref HEAD refs/heads/[name]
  $ rm .git/index
  $ git clean -fdx

版本(tag)操作相关命令::

  查看版本：$ git tag
  创建版本：$ git tag [name]
  删除版本：$ git tag -d [name]
  查看远程版本：$ git tag -r
  创建远程版本(本地版本push到远程)：$ git push origin [name]
  删除远程版本：$ git push origin :refs/tags/[name]
  合并远程仓库的tag到本地：$ git pull origin --tags
  上传本地tag到远程仓库：$ git push origin --tags
  创建带注释的tag：$ git tag -a [name] -m 'yourMessage'

子模块(submodule)相关操作命令::

  添加子模块：$ git submodule add [url] [path]
      如：$ git submodule add git://github.com/soberh/ui-libs.git src/main/webapp/ui-libs
  初始化子模块：$ git submodule init  ----只在首次检出仓库时运行一次就行
  更新子模块：$ git submodule update ----每次更新或切换分支后都需要运行一下
  删除子模块：（分4步走哦）
   1) $ git rm --cached [path]
   2) 编辑“.gitmodules”文件，将子模块的相关配置节点删除掉
   3) 编辑“ .git/config”文件，将子模块的相关配置节点删除掉
   4) 手动删除子模块残留的目录

忽略一些文件、文件夹不提交::

  在仓库根目录下创建名称为“.gitignore”的文件，写入不需要的文件夹名或文件，每个元素占一行即可，如
  target
  bin
  *.db

后悔药::

  删除当前仓库内未受版本管理的文件：$ git clean -f
  恢复仓库到上一次的提交状态：$ git reset --hard
  回退所有内容到上一个版本：$ git reset HEAD^
  回退a.py这个文件的版本到上一个版本：$ git reset HEAD^ a.py
  回退到某个版本：$ git reset 057d 
  将本地的状态回退到和远程的一样：$ git reset –hard origin/master  
  向前回退到第3个版本：$ git reset –soft HEAD~3

Git一键推送多个远程仓库::

  编辑本地仓库的.git/config文件：
  [remote "all"]
      url = git@github.com:dragon/test.git
      url = git@gitcafe.com:dragon/test.git
  这样，使用git push all即可一键Push到多个远程仓库中。

