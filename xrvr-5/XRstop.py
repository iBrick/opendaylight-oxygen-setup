#!/usr/bin/env python

import os

processes = os.popen('sudo ps -ef | grep XR')
for process in processes:
	words = process.split()
	if words[7] == 'qemu-system-x86_64':
		os.popen('sudo kill -9 ' + words[1])
