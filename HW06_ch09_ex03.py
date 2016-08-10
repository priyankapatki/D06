#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import operator

# Body


def avoids(word, forbid_str):
    """ return True if word NOT forbidden"""
    if any((c in forbid_str) for c in word):
        return False
    else:
        return True


def forbidden_prompt(file_name):
    """ print count of words NOT forbidden by input"""
     # Enter forbid_arg in format = a,b,c
    user_input = str(input("Please enter a string of forbidden letters seperated by comma: "))
    forbid_str = user_input.split(',')
    with open(file_name, 'r') as f:
        word_list = f.readlines()
    limit = len(word_list)

    for count in range(0, limit):
        result = avoids(word_list[count], forbid_str)
        if result == True:
            print(word_list[count])


def forbidden_param(file_name, forbid_arg):  
    # Enter forbid_arg in format = 'a,b,c'
    #""" return count of words NOT forbidden by param"""
    forbid_str = forbid_arg.split(',')
    with open(file_name, 'r') as f:
        word_list = f.readlines()
    limit = len(word_list)

    for count in range(0, limit):
        result = avoids(word_list[count], forbid_str)
        if result == True:
            print(word_list[count])

def alphabet_list():
    alpha_lst = [' ']*26
    start = ord('a')
    for count in range(0, 26):
        alpha_lst [count] = chr(start) 
        start += 1
    return alpha_lst

def find_five(file_name):
      
    with open(file_name, 'r') as f:
        all_alpha = alphabet_list()   # all_alpha is a list of all alphabets
        f_lines = f.readlines()      # f_lines is a list of all the lines in the file
        limit = len(f_lines)
        word_dict = dict()           # list maintains a count of words every alphabet appears in
                            
        for count in range(0, 26):    # The outer loop maintains the count for alphabet list
            word_cnt = 0           # letter_cnt will hold the count of words a letter appears in
            for line_count in  range(0, limit):  # The inner loop goes over every line in the file
                if all_alpha[count] in f_lines[line_count]:   # condition to check each letter in line
                    word_cnt += 1
            word_dict[chr(ord('a') + count)] = word_cnt    # associating the letter with the number of words
                                              
                                                             # the letter appears in 
    words_final = sorted(word_dict.items(), key=operator.itemgetter(1))   # sorting the items

    for count in range(0, 5):  # selecting 5 letters occuring in least number of words
        print('The letter {} appears in {} words'.format(words_final[count][0], repr(words_final[count][1])))


##############################################################################
def main():
    # Your final submission should only call five_five
    # print("\n avoids:")
    # print(avoids('abcd', ('f','g')))
    # print("\n forbidden_prommpt:")
    # forbidden_prompt('words.txt')
    # print("\n forbidden_param:")
    # forbidden_param('words.txt', 'a,b,c')
    print("\n find_five:")
    find_five('words.txt')


if __name__ == '__main__':
    main()
