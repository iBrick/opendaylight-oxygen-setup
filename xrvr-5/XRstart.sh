#!/bin/bash

while read -r line
do
	sudo ./$(echo $line | cut -f2 -d" ").sh
done < nodes
