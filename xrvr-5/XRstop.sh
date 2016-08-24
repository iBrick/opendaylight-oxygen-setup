#!/bin/bash

source ./parameters

while read -r line
do
	name=$(echo $line | cut -f2 -d" ")
	sudo kill -9 $(ps aux | grep 'qemu-system-x86_64' | grep $name | awk '{print $2}')
done < nodes
