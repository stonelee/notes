.. _html:


***************
html
***************


label for对应input id

input name在submit时提交

语义化
===========

<!Doctype html>

为关键链接添加 accesskey::

  <a href="" title="" accesskey="M" rel="">Link</a>

abbr应该添加一个 title 属性对缩写进行描述::

  <abbr title="Web Developer" >WD</abbr>

大段引用: <blockquote>，一般引用: <cite>

删除：<del>

定义列表：<dl>

格式化片段 <code>/<pre>，<pre> 的范围更广

强调: strong > em ≈ cite

表单项:<label for="firstname">

<img src="" alt="替代文本" />

html5
================

::

  <header id="page-header">
    <h1>Site title</h1>
    <form>Search</form>
    <nav class="site-nav">
      <ul>Site navigation</ul>
    </nav>
  </header>
  <section id="main-content">
    <article>
      <h1>Article title</h1>
      <p>Summary</p>
    </article>
    <article>
      <h1>Article title</h1>
      <p>Summary</p>
    </article>
    <article>
      <h1>Article title</h1>
      <p>Summary</p>
    </article>
  </section>
  <aside class="sidebar">
    <section>
      <h2>Blogroll…</h2>
    </section>
    <section>
      <h2>Photos…</h2>
    </section>
  </aside>
  <footer id="page-footer">
    <h2>Footer</h2>
  </footer>

div, section, article::

  div block-level element，没有语义
  section 关联部分的集合，例如文章的一部分，页面的一部分
  article 可独立的完整的部分，例如一篇文章，论坛的一篇帖子或者评论
  article是特殊的section，section是特殊的div
  article和section可以互相包含

header, hgroup & h1-h6::

  header 可以包含h1-h6,hgroup等其他元素，可以出现在任何位置，除了footer和header
  hgroup 特殊的header，只能包含h1-h6，用来分组子标题

<nav>, <aside>, <figure> and <footer>::

  nav 主要导航链接，footer中的不算，有利于可访问性
  aside 侧边栏，脚注等起辅助作用的部分
  figure 内容重要，但是位置不重要。多用于images, video, graph, code sample 等使用css position定位的部分

The sectioning content elements are <section>, <article>, <nav> and <aside>

