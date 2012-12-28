.. _centos:

***************
CentOS
***************

安装
---------

虚拟机VirtualBox安装CentOS 6.3

安装报错::

  this kernel requires the following features not present on the cpu pae

在虚拟机的“设置”/“系统”/“处理器”中勾选“启用PAE/NX”，再重新启动虚拟机即可。

添加用户::

  useradd stonelee
  passwd stonelee

切换用户::

  su stonelee

临时更改主机名::

  hostname CentOS

上网
---------------

virtualbox网络连接方式为桥接网卡

重新启动网络配置::

  service network restart

修改 IP 地址::

  /etc/sysconfig/network-scripts/ifcfg-eth0

  BOOTPROTO=static #设置网卡获得ip地址的方式，可能的选项为static，dhcp或bootp，分别对应静态指定的 ip地址，通过dhcp协议获得的ip地址，通过bootp协议获得的ip地址
  IPADDR=10.10.22.83 #如果设置网卡获得 ip地址的方式为静态指定，此字段就指定了网卡对应的ip地址
  NETMASK=255.255.255.0 #网卡对应的网络掩码
  ONBOOT=yes #系统启动时是否设置此网络接口，设置为yes时，系统启动时激活此设备

修改网关 Default Gateway::

  /etc/sysconfig/network

  GATEWAY=10.10.22.1

修改 DNS::

  /etc/resolv.conf

  nameserver 208.67.220.220
  nameserver 8.8.8.8

能上内网不能上外网
====================

原因:缺少路由配置::

  /etc/sysconfig/network-scripts 新建文件 route-eth0
  内容：via 192.168.1.1（网关地址）

更新源
===========

关闭fastestmirror::

  /etc/yum/pluginconf.d/fastestmirror.conf

  enabled=0

使用中科大源::

  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.old
  下载对应版本repo文件: http://mirrors.163.com/.help/CentOS6-Base-163.repo
  或者将里面的网址换为中科大的：centos.ustc.edu.cn

  yum clean all
  yum upgrade
  yum -y update

  生成缓存:
  yum makecache

配置防火墙
=============

开放80端口::

  iptables -A INPUT -p tcp --dport 80 -j ACCEPT

查看规则::

  iptables -L -n

查看规则对应的编号::

  iptables -L -n --line-number

删除规则::

  iptables -D INPUT 2

保存规则::

  #实际保存到 /etc/sysconfig/iptables
  service iptables save

重启::

  service iptables restart

常用软件
------------

更改bashrc, inputrc

yum install git vim-enhanced man

Debian/Ubuntu中安装常用编译工具::

  apt-get install build-essentials

CentOS中::

  yum groupinstall "Development Tools"
  yum install kernel-devel kernel-headers

nginx 403 forbidden
=======================

nginx.conf中配置user为网站目录所有者::

  user stonelee;

网站目录配置执行权限::

  chmod -R 755 html/

查看::

  ls -l html/

结果::

  -rwxr-xr-x. 1 stonelee stonelee 342 Dec 26 09:59 index.html
