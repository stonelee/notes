.. _server:


***************
部署
***************

mod_wsgi
=============================

::

	$ yum install mod_wsgi
	$ yum install httpd

httpd默认绑定80端口

uwsgi together with nginx
=============================

nginx  pass requests to the uWSGI server.
http://projects.unbit.it/uwsgi/

