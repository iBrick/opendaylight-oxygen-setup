#!/bin/bash

source ./parameters

i=0
j=1
while read -r line
do
	let "i++"
	addr=$(echo $line | cut -f1 -d" ")
	name=$(echo $line | cut -f2 -d" ")
	./XRloader.exp $name $addr $PORT_PREFIX$i$j
done < nodes
