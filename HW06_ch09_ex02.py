#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
    if 'e' not in word:
        return True
    else:
        return False

def count_lines(file_name):
    with open(file_name, 'r') as f:
        total_lines = len(f.readlines())
        return total_lines


def print_no_e(file_name):
    with open(file_name, 'r') as f:
        count = 0
        line = f.readline()
        #total_words = len(f.readlines())
        for line in f:
            return_value = has_no_e(line)
            if return_value == True:
                print(line.strip('\n') + '%')
                count += 1

    total_words = count_lines(file_name)

    print('Number of approved words = {}'.format(count))
    print('Total number of words = {}'.format(total_words))
    percent_words = (count/total_words) * 100
    print('Percentage of approved words = {}'.format(percent_words))


##############################################################################
def main():
      # Call your function(s) here
    print_no_e('words.txt')

if __name__ == '__main__':
    main()
