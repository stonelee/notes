.. _rails:

***************
rails
***************

安装ROR环境
====================

安装RVM::

  $ curl -L get.rvm.io | bash -s stable
  $ source ~/.bash_profile

  $ rvm -v

用 RVM 安装 Ruby 环境(Ruby, Ruby Gems)::

  $ rvm pkg install readline
  $ rvm install 1.9.2 --with-readline-dir=$rvm_path/usr

设置 Ruby 版本::

  $ rvm 1.9.2 --default

  $ ruby -v
  ruby 1.9.2p290 (2011-07-09 revision 32553) [x86_64-darwin10.8.0]

  $ gem -v
  1.8.6

或者创建gemset，来管理多个rails和gem::

  $ rvm use 1.9.3
  $ rvm gemset create rails313
  $ rvm use 1.9.3@rails313

  # 查看目前所在环境
  $ rvm list
  $ rvm gemset list

设置速度更快的taobao源::

  $ gem source -r http://rubygems.org/
  $ gem source -a http://ruby.taobao.org

安装Rails以及依赖管理工具Bundler::

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

执行db/seeds.rb生成数据::

  $ rake db:seed

更新数据库结构::

  $ rake db:migrate

回滚migrate::

  $ rake db:rollback

重建数据库::

  $ rake db:reset

列出所有命令::

  rake -T

删除数据库::

  rake db:drop

生成数据库::

  rake db:schema:load

测试::

  $ rake test
  $ rake test:units

sqlite命令行,line参数使得排列比较美观::

  sqlite3 -line db/development.sqlite3

执行脚本::

  rails runner script/load_orders.rb

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

migrate用来添加数据表，更改数据表结构，更改相应数据内容

心得
===============

数据表字段名不能为：type

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

twitter-bootstrap-rails
===========================

https://github.com/seyhunak/twitter-bootstrap-rails

在Gemfile中加入::

  gem 'twitter-bootstrap-rails', :git => 'git://github.com/seyhunak/twitter-bootstrap-rails.git'

然后::

  bundle install

加入bootstrap js、css文件::

  rails g bootstrap:install

改变application样式::

  rails g bootstrap:layout application fixed

更改scaffold样式::

  rails g scaffold Post title:string description:text
  rake db:migrate
  rails g bootstrap:themed Posts

virtualbox中安装centos
===========================

64位环境需要在bios中打开vt，然后关机，然后开机

上网
--------------------------

连接方式使用NAT

获取网络配置::

  dhclient -v eth0

Host使用ssh访问Guest

Port Forwarding中设置

==== ======== ===================== ========= =====================
Name Protocol Host IP     Host Port Guest IP  Guest Port
==== ======== ===================== ========= =====================
ssh  TCP      10.10.22.84 2222      10.0.2.15 22
==== ======== ===================== ========= =====================

Host中连接::

  ssh -l root -p 2222 10.10.22.84

注意：linux中因为权限问题，应该设置host port大于1024.

上传文件::

  scp -P 2222 /home/stonelee/Downloads/CentOS6-Base-163.repo root@10.10.22.84:/

ping 8.8.8.8

NAT网络的连接方式的优点就是方便配置，无须手动设置IP等，自动获取就行了。 虚拟机能访问网络。 虚拟机与Host机之间也能互相访问。 但外部网站无法访问虚拟机（缺点）

http://chenling1018.blog.163.com/blog/static/14802542010431102339538/
http://www.cnblogs.com/chusiping/archive/2011/11/09/2243467.html

更新163源
---------------

备份::

  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

下载对应版本repo文件: http://mirrors.163.com/.help/CentOS6-Base-163.repo

::

  yum clean all
  yum upgrade
  yum -y update

生成缓存::

  yum makecache

部署
==============

Rails为单线程, Apache作为前端服务器处理请求，使用Passenger代理到后端多个rails实例中处理

使用Phusion Passenger部署到apache上
-----------------------------------------

::

  $ gem install passenger
  $ passenger-install-apache2-module

在/etc/httpd/conf中添加::

  LoadModule passenger_module /home/stonelee/.rvm/gems/ruby-1.9.3-p194@rails323/gems/passenger-3.0.14/ext/apache2/mod_passenger.so
  PassengerRoot /home/stonelee/.rvm/gems/ruby-1.9.3-p194@rails323/gems/passenger-3.0.14
  PassengerRuby /home/stonelee/.rvm/wrappers/ruby-1.9.3-p194@rails323/ruby

  NameVirtualHost *:80
  Listen 80

  <VirtualHost *:80>
    ServerName depot.yourhost.com
    DocumentRoot /home/stonelee/test/rails32/depot_v/public
    <Directory /home/stonelee/test/rails32/depot_v/public>
      AllowOverride all
      Options -MultiViews
      Order allow,deny
      Allow from all
    </Directory>
  </VirtualHost>

/etc/hosts中设置域名::

  127.0.0.1 depot.yourhost.com

然后::

  service httpd restart

需要关闭selinux

如果报权限错误，需要在home目录加Read and Execute permissions::

  sudo chmod o+rx /home/joarobles

生产数据库
---------------

Gemfile::

  group :production do
    gem 'mysql2'
  end

config/database.yml::

  production:
    adapter: mysql2
    encoding: utf8
    reconnect: false
    database: depot_production
    pool: 5
    username: username
    password: password
    host: localhost

::

  mysql -u root -p
  create database depot_production;

创建表结构::

  rake db:setup RAILS_ENV="production"

assets预压缩::

  bundle exec rake assets:precompile

Capistrano部署到远程
---------------------------------

在生产服务器创建代码仓库::

  $ git --bare init

开发服务器设置推送地址::

  git remote add origin ssh://root@10.10.22.84:2222/~/git/depot.git
  git push origin master

报错::

  Host key verification failed.

重新ssh进入，提示保存known hosts

config/deploy.rb中::

  default_run_options[:pty] = true
  ssh_options[:forward_agent] = true

生产服务器需要安装rvm，ruby，安装依赖::

  yum install -y gcc-c++ patch readline readline-devel zlib zlib-devel libyaml-devel libffi-devel openssl-devel make bzip2 autoconf automake libtool bison iconv-devel

