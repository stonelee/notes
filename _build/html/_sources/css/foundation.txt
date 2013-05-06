.. _foundation:


***************
foundation
***************

box-sizing: border-box 简化width的计算

768px为分隔

grid
===============

row::

  .row 整行

    width: 100%; //窄屏100%宽度
    max-width: 62.5em; //宽屏固定大小
    margin: 0 auto; //居中

  嵌套row（.row .row ）

    width: auto;
    max-width: none;
    左右margin补偿columns的padding

columns::

  行中的列需要.columns，一行12列，如果超出12则显示为下一行

  position: relative; //为定位准备
  float: left; //左浮动
  有左右padding

  如果设置了多个column，最后一个右浮动。即如果不满足12实现两端浮动效果
  [class*="column"] + [class*="column"]:last-child {
    float: right;
  }


  .large-* 设置宽屏中比例，如果只设large-*则窄屏中显示为整行
  .small-* 设置窄屏中比例，如果只设small-*则宽屏中也按该比例显示
  百分比宽度


  .show-for-small 在窄屏中显示
  .hide-for-small 在宽屏中显示
  如果不设置则宽屏窄屏中都显示

  .large-offset-* 和 .small-offset-* 通过margin-left进行偏移


  small-centered 窄屏中整行居中，宽屏中无居中效果，也没有偏移
  large-centered 宽屏中整行居中，窄屏中无效

  .push-* 宽屏中通过设置百分比left将元素推向右边
  .pull-* 宽屏中通过设置百分比right将元素拉向左边

