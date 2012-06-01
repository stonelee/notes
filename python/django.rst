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

技巧
=============================
要保证table中的columns多于等于model中的fields

date和numeric field需要同时设置null=True, blank=True. 字符field可以blank=True，这样默认会保存为""

__name__可以得到class的name

extra URLConf优先于url中捕获的参数

view中捕获的参数都是字符类型的，因此default value也最好设为字符型

post之后要HtpResponseRedirect防止重复提交

防报错:kwargs.pop('GET',None)

auto escape会影响：

===	===
<	&lt;
>	&gt;
'	&#39;
"	&quot;
&	&amp;
===	===

防止escape

{{ data|safe }}

{% autoescape off %}

要注意filter arguments不会被自动编码
{{ data|default:"3 &lt; 2" }}

改变数据时使用post，仅仅查询或显示使用get

form显示和提交往往可以使用同一个view，这时<form action="" method="get">即可。

forms framework:HTML display, validation, data cleanup and form redisplay-with-errors.

* Field classes：validation logic
* widgets：presentation logic.

::

	def contact(request):
		if request.method == 'POST':
			form = ContactForm(request.POST)
				if form.is_valid():
					cd = form.cleaned_data
					return HttpResponseRedirect('/contact/thanks/')
		else:
			form = ContactForm(
				#使用initial设置初始值，unbound，不会造成error：
				initial={'subject': 'I love your site!'}
			)
		return render_to_response('contact_form.html', {'form': form})

widget::

	from django import forms
	class ContactForm(forms.Form):
		subject = forms.CharField(max_length=100)
		email = forms.EmailField(required=False, label='Your e-mail address')
		message = forms.CharField(widget=forms.Textarea)

自定义校验::

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message

第三方库
=============================

django-cms
------------------------

报错::

	admin/change_list.py: Negative indexing is not supported

解决：django-mptt降级到0.5.1::

	$ pip install django-mptt==0.5.1 --upgrade

查看版本号::

	$ pip freeze


django-extensions
------------------------

安装图形库::

	yum install graphviz
	yum install graphviz-devel

	pip install pygraphviz

生成数据库模型图::

	$python ./manage.py graph_models -a -g -o my_project_visualized.png

查看图片::

	$ display some.png

django-mptt
---------------------
https://github.com/django-mptt/django-mptt/

预排序遍历树 Modified Preorder Tree
Traversal（MPTT）,可以非常有效率的进行树的检索
http://www.cnblogs.com/woodcutter/archive/2010/04/21/1716923.html

---------------------

更换主题: https://github.com/MegaMark16/django-cms-themes

blog: https://github.com/Fantomas42/django-blog-zinnia
貌似有很多可重用的模块供学习

vim下python工具集合，用于配置python开发环境
https://github.com/klen/python-mode

基于django和Bootstrap管理mongodb的网站工具，可以从中学习使用bootstrap的经验
http://thomasst.ch/mongoadmin/

Pandoc-多种写作格式转换
http://johnmacfarlane.net/pandoc/

django-rest-framework
https://github.com/tomchristie/django-rest-framework
自描述 browse-able restful web apis
