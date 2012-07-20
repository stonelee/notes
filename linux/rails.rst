.. _rails:

***************
rails
***************

安装ROR环境
====================

1. 安装RVM::

	$ curl -L get.rvm.io | bash -s stable
	$ source ~/.bash_profile

	$ rvm -v

#. 用 RVM 安装 Ruby 环境(Ruby, Ruby Gems)::

	$ rvm pkg install readline
	$ rvm install 1.9.2 --with-readline-dir=$rvm_path/usr

#. 设置 Ruby 版本::

	$ rvm 1.9.2 --default

	$ ruby -v
	ruby 1.9.2p290 (2011-07-09 revision 32553) [x86_64-darwin10.8.0]

	$ gem -v
	1.8.6

#. 或者创建gemset，来管理多个rails和gem::

	$ rvm use 1.9.3
	$ rvm gemset create rails313
	$ rvm use 1.9.3@rails313

	# 查看目前所在环境
	$ rvm list
	$ rvm gemset list

#. 设置速度更快的taobao源::

	$ gem source -r http://rubygems.org/
	$ gem source -a http://ruby.taobao.org

#. 安装Rails以及依赖管理工具Bundler::

	$ gem install bundler rails

	$ bundle -v
	Bundler version 1.0

	$ rails -v
	Rails 3.2.1

自动加载环境
------------------

在项目目录中建立.rvmrc文件, 加入::

	rvm use 1.9.3@rails313

这样在进入项目目录后，会自动加载对应版本ruby和gemset

rails开发
==================

常用命令
---------

加载环境::

	$ rvm use 1.9.3@rails323

建立项目::

	$ rails new blog

运行服务器::

	$ rails server

model命令行::

	$ rails console

初始化数据，执行seeds文件中的代码::

	$ rake db:seed

更新数据库结构::

	$ rake db:migrate

回滚migrate::

	$ rake db:rollback

重建数据库::

	$ rake db:reset

测试::

	$ rake test
	$ rake test:units

自动生成
-------------

首页（the home controller’s index action）::

	$ rails generate controller home index

为新的resource生成models, views, and controllers::

	$ rails generate scaffold Post name:string title:string content:text

创建model::

	$ rails generate model Comment commenter:string body:text post:references

创建controller::

	$ rails generate controller Comments

笔记
-------------

cookie中保存sessionId，用来到服务端找到对应的session，默认使用CookieStore，可以防篡改但是没有加密，只有4k，建议存简单objects

api中后面有!的（如save!）当有问题时抛出异常


心得
===============

生成本地 Rails Guides
----------------------------
::

	$ rake doc:guides 

提示以下错误信息::

	cannot load such file -- redcloth

需要在 Gemfile 里添加::

	gem 'RedCloth'

然后执行::

	bundle

或者::

	gem install RedCloth

