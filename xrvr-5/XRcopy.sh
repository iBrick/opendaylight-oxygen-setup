#!/bin/bash

while read -r line
do
	cp $1 ./$(echo $line | cut -f2 -d" ").vmdk
done < nodes
