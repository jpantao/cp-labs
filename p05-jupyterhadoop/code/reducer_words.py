#!/usr/bin/python

import sys

total_count = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, count = line.split('\t', 1)
    
    if key not in total_count:
        total_count[key] = 0
        
    # convert count (currently a string) to int
    total_count[key] += int(count)

for key in total_count:
    print(f'{key}\t{total_count[key]}')

