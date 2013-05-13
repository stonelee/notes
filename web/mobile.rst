.. _mobile:


***************
mobile
***************

改变程序图标::

  convert -resize 96x96! heart.png E:\mobile\love\res\drawable\icon.png
  convert -resize 72x72! heart.png E:\mobile\love\res\drawable-hdpi\icon.png
  convert -resize 36x36! heart.png E:\mobile\love\res\drawable-ldpi\icon.png
  convert -resize 48x48! heart.png E:\mobile\love\res\drawable-mdpi\icon.png
  convert -resize 96x96! heart.png E:\mobile\love\res\drawable-xhdpi\icon.png

静态页面在assets中

::

  E:\mobile\phonegap-master\lib\android\bin\create.bat E:\mobile\love info.stonelee.love Love


导入魔兽人物动作
----------------------

1. Warcraft 3 Viewer v2.3

选择max模型，这里选择Units/Human/Jaina/Jaina.mdx。
Animation选择Attack

2. 调整

将显示框拉到最小（TODO：尽量减少空白）。
背景色选为白色。
坐标轴去掉。

3. ImageMagick

将所有img00开头的文件进行合并，将白色设为透明背景，合并为1行，每个文件大小为121*98，没有间隔，导出为png格式::

  montage img00*.jpg -background transparent -transparent #fff -tile x1 -geometry 121x98+0+0 player.png


