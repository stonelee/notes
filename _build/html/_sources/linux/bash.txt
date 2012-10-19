.. _bash:


***************
bash
***************

将文件夹内所有js文件打包成all.js::

  $ find . -type f -name "*.js" -exec cat {} \; > all.js

统计文件夹内所有coffee文件的代码行数::

  $ find . -type f -name "*.coffee" -print0|xargs -0 wc -l

取文件名::

	$basename /etc/passwd => passwd

取文件路径::

	$dirname /etc/passwd => /etc

循环遍历文件夹里的文件::

	#!/bin/bash

	allFiles() {
		for file in $1/*
		do
			if [ -d $file ]; then
				allFiles $file
			else
				echo $file
			fi
		done
	}

	testdir=/path/to/test/dir
	allFiles $testdir

删除最后一个字符::

	files=${files%?}

