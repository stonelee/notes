.. _jekyll:


***************
jekyll
***************

安装jekyll::

	$ gem install jekyll 0.11.0

遇到问题::

	Liquid error: undefined method `join’ for #

解决：liquid降级::

	$ gem uninstall liquid
	$ gem install liquid -v 2.2.2

查看生成html时的错误::

	$ jekyll --no-auto --server
