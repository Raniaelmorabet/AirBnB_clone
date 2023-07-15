#!/bin/bash

# List all Python files in the current directory and its subdirectories
files=$(find . -name "*.py")

# Loop through each file and check its style
for file in $files; do
    echo "Checking style for $file"
    pycodestyle "$file"
done
