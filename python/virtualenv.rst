.. _virtualenv:


***************
virtualenv
***************

基本命令
=============================

`下载 <http://pypi.python.org/pypi/virtualenv#downloads>`_
解压缩即可使用。

创建虚拟环境ENV::

	$ python virtualenv.py ENV

在ENV/bin中已经安好了pip,使用的python是系统python版本。

进入bin，使用pip安装其他库::

	$ ./pip install -U mezzanine

会自动安装依赖库，其中Pillow库需要::

	$ yum install dpkg-devel，python-devel

进入虚拟环境，这样就可以直接使用python之类的程序::

	$ source mysite-env/bin/activate

mezzanine
=============================

创建::

	# Create a project
	$ mezzanine-project myproject
	$ cd myproject

	# Create a database
	$ python manage.py createdb

	# Run the web server
	$ python manage.py runserver

pinax
=============================

安装::

	(mysite-env)$ pip install Pinax

创建::

	(mysite-env)$ pinax-admin setup_project mysite

查看可以创建的模板pinax::

	(mysite-env)$ pinax-admin setup_project -l

创建其它pinax::

	(mysite-env)$ pinax-admin setup_project -b basic mysite

