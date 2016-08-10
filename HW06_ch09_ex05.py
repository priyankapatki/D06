#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports

# Body
def uses_all(word, letter_str):
    for letter in letter_str:
        if letter not in  word:
            return False
    else:
        return True

def vowel(filename, word):
    with open(filename, 'r') as f:
        word = word.split(',')
        line = f.readline()
        count = 0

        for line in f:
            if uses_all(line, word) == True:
                count += 1

        print('# of words that use all {}: {}'.format((word),repr(count)))


##############################################################################
def main():
     # Call your function(s) here.
     vowel('words.txt', 'a,e,i,o,u')
     vowel('words.txt', 'a,e,i,o,u,y')



if __name__ == '__main__':
    main()
