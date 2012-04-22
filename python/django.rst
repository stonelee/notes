.. _django:


***************
django
***************

基本命令
=============================

创建::

	django-admin.py startproject kjdjango
	python manage.py startapp personnels

运行::

	python manage.py runserver

查看数据库生成SQL::

	python manage.py sql personnels

创建数据库::

	python manage.py syncdb

试验sql语句::

	python manage.py shell

生成初始化数据
=============================

#. 进入admin操作，插入一些数据

#. 将personnels中的数据内容生成到该app下的fixtures文件夹里::

	python manage.py dumpdata personnels > personnels/fixtures/initial_data.json

#. 每次python manage.py syncdb都会重新生成这些数据

发布静态文件
=============================

代码::

	./manage.py collectstatic

