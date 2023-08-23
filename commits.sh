#!/bin/bash

for ((i=1; i<=40; i++))
do
    echo "Commit $i" > file.txt
    git add file.txt
    git commit -m "Commit $i"
done
