.. _css3:


***************
css3
***************

基本属性
----------

阴影box-shadow::

  横偏移 竖偏移 阴影大小 颜色
  -webkit-box-shadow:0 15px 10px rgba(0, 0, 0, 0.7);
  -moz-box-shadow:0 -15px 10px rgba(0, 0, 0, 0.7);
  box-shadow:10px 15px 10px rgba(0, 0, 0, 0.7);

旋转transform::

  -3逆时针
  -webkit-transform:rotate(-3deg);
  -moz-transform:rotate(-3deg);
  -o-transform:rotate(-3deg);
  transform:rotate(-3deg);

pointer-events::

  设置该元素是否响应鼠标事件，设为none则元素不再是鼠标事件的目标，鼠标不再监听当前层而去监听下面层中的元素。
  如果它的子元素设置为auto，鼠标还是会监听这个子元素的。
  用于google地图的导航区域

渐进增强与平稳退化
------------------

平稳退化 (Graceful Degradation)于1994 年提出，由于其并不真正互联网符合普及的可访问型 Web (Universally Accessible Web)”的设计初衷。
2003 年提出渐进增强 (Progressive Enhancement)，聚焦于内容并能为旧设备提供更多实际支持，
从而改善内容可利用性 (Content Availability)、全局可访问性 (Overall Accessibility) 和移动设备浏览器的能力。

它们是看待同种事物的两种观点，都关注于同一网站在不同设备里不同浏览器下的表现程度。
关键的区别则在于它们各自关注于何处，以及这种关注如何影响工作的流程。

"平稳退化”观点认为应该针对那些最高级、最完善的浏览器来设计网站。
而将那些被认为“过时”或有功能缺失的浏览器下的测试工作安排在开发周期的最后阶段，
并把测试对象限定为主流浏览器（如 IE、Mozilla 等）的前一个版本。
在这种设计范例下，旧版的浏览器被认为仅能提供“简陋却无妨 (poor, but passable)” 的浏览体验。
你可以做一些小的调整来适应某个特定的浏览器。
但由于它们并非我们所关注的焦点，因此除了修复较大的错误之外，其它的差异将被直接忽略。

“渐进增强”观点则认为应关注于内容本身.即从内容出发。
内容为样式和交互构建起坚实的基础，由上至下分别为：“内容”、“表现”和“客户端脚本”。

这种开发方式被称为“无侵入 (Unobtrusive)

实例
----------

文字阴影：text-shadow: 1px 1px white;（右下白色阴影）

圆角：border-radius: 3px; （按钮3px，文本框6px）

盒阴影：box-shadow: 1px 2px 3px rgba(0, 0, 0, .5);（右下透明阴影）

渐变背景: background:-webkit-linear-gradient(top , #F2F2F2, #ffffff 8px);（按钮、标题栏、控件背景）

CSS选择器、伪类：li:first-child{border-top:0;}（去掉第一个li的top border）

input:focus {border-color:#a0b3d6;}（IE6、7不支持）

text-overflow：ellipsis （文字溢出特定宽度“点点点”省略号表示）

图片渐入: -webkit-transition: all 0.3s ease-out 0s;

图片旋转: -webkit-transform: rotate(360deg);

