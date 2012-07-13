.. _bash:


***************
bash
***************


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

