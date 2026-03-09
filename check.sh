#!/bin/bash
set -e

echo "Checking disk space..."
df -h

echo "Checking memory..."
free -m
cat fakefile.txt
echo "Done."
