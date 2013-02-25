.. _phonegap:

***************
PhoneGap
***************

jre中::

  keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

PhoneGap使用
-------------

环境变量中加入android sdk，jdk，ant::

  E:\mobile\adt-bundle-windows-x86\sdk\platform-tools;
  E:\mobile\adt-bundle-windows-x86\sdk\tools;
  D:\Program Files\Java\jdk1.6.0_20\bin;
  E:\mobile\apache-ant-1.8.4\bin;


创建工程::

  E:\mobile\phonegap-master\lib\android\bin\create.bat E:\mobile\my_project info.stonelee.demo Demo

报错：没有文件扩展“.js”的脚本引擎。
注册表把[HKEY_CLASSES_ROOT\.js] 项下的那个默认值改成 "JSFile" 就可以正常运行JS 文件了.

build::

  $ /path/to/my_new_cordova_project/cordova/build.bat

