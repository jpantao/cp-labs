#!/usr/bin/env python


# import sys
import sys
# import string library function  
import string  

word_freq = {}

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
   
    word, count = line.split('\t', 1)
    word_freq[word] = int(count)
    
sorted_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
for key in word_freq:
    print(f'{key}\t{word_freq[key]}')

