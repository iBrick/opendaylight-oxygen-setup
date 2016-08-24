#!/bin/bash

while read -r line
do
	name=$(echo $line | cut -f2 -d" ")
	echo $name
	cp $1 ./$name.iso
done < nodes
