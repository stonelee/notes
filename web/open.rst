.. _open:


***************
开放平台
***************

douban
-------------

1.事先申请
===========

======= ====================================
API Key	097ee65eeca0a0331c7cb31cc5e1e099
Secret	fcc8e706abfe1868
======= ====================================

2.获取authorization_code
============================

get，参数为API key::

  https://www.douban.com/service/auth2/auth?client_id=097ee65eeca0a0331c7cb31cc5e1e099&redirect_uri=https://www.example.com/back&response_type=code

用户在豆瓣页面授权，然后跳转页面，url中返回authorization_code::

  https://www.example.com/back?code=d899f459b09e3146

code='d899f459b09e3146'

3.获取access_token
====================

post提交，参数为API Key，secret，authorization code::

  tokenUrl='https://www.douban.com/service/auth2/token'
  $.post(tokenUrl,{
    client_id: '097ee65eeca0a0331c7cb31cc5e1e099',
    client_secret:'fcc8e706abfe1868',
    redirect_uri:'https://www.example.com/back',
    grant_type:'authorization_code',
    code:code
    },function(data){
    console.log(data);
  });

返回access_token::

  {"access_token":"35caf4330baeb630a160dc99230c2290","douban_user_id":"67590112","expires_in":604800,"refresh_token":"78e6fdc92d43d9826ab4f95b87cb8c86"}

4.调用其他API：
=================

在header中添加Authorization:Bearer 35caf4330baeb630a160dc99230c2290，然后直接发请求::

  curl "https://api.douban.com/v2/user/~me" -H "Authorization:Bearer 35caf4330baeb630a160dc99230c2290"
  curl "https://api.douban.com/v2/book/20383605/collection" -H "Authorization:Bearer 35caf4330baeb630a160dc99230c2290" -X POST -i -v

或::

  $.ajax({
    type: 'GET',
    url:'douban/api/user/~me',
    headers: {
      Authorization: 'Bearer 35caf4330baeb630a160dc99230c2290'
    },
    success:function(data){
      console.log(data);
    }
  });

