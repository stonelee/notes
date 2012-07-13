.. _octopress:


***************
octopress
***************

1.安装rvm::

	bash -s stable < <(curl -s https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer)
	echo '[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm" # Load RVM function' >> ~/.bash_profile
	source ~/.bash_profile

2.安装ruby::

	rvm install 1.9.2 && rvm use 1.9.2
	rvm rubygems latest

3.安装Octopress::

	git clone git://github.com/imathis/octopress.git octopress
	cd octopress    # If you use RVM, You'll be asked if you trust the .rvmrc file (say yes).
	ruby --version  # Should report Ruby 1.9.2

4.安装依赖::

	gem install bundler
	bundle install

5.安装主题::

	bundle exec rake install

6.本地预览::

	bundle exec rake preview 

7.生成目录结构::

	bundle exec rake setup_github_pages
	Enter the read/write url for your repository:
	(git@github.com:stonelee/stonelee.github.com.git)

8.部署::

	bundle exec rake generate
	bundle exec rake deploy

9.源码版本控制::

	git add .
	git commit -m 'init'
	git push origin source


10.开始写blog::

	rake new_post["title"]

bug
--------------------
指定code渲染模式时发生错误::

	in `block in ffi_lib': Could not open library 'lib.so': lib.so: cannot open
	shared object file: No such file or directory (LoadError)

解决方案:

将Gemfile.lock的rubypython改为0.5.3, 然后::

	bundle install

http://www.dejaaugustine.com/2011/10/rubypython-on-64-bit-rhel5centos/

textile转markdown
---------------------
::

	pandoc index.textile -o index.markdown
