# import sys
import sys
# import string library function  
import string  

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # remove punctuation characters
    line = line.translate(str.maketrans('', '', string.punctuation+'«»'))
    # split the line into words
    words = line.split()
    
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    
for key in word_freq:
    print(f'{key}\t{word_freq[key]}')

