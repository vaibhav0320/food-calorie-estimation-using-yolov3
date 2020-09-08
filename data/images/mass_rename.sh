#!/bin/bash
i=1
for file in *.jpg;do
	mv $file kiwi$i.jpg
	let i=i+1
done
