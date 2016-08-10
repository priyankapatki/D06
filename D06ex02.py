#!/usr/bin/env python3
import random


# def random_nos(count):
#     with open('random_nos.txt', 'w') as f:
#         for n in range(1, count + 1):
#             f.write(str(random.randint(100, 250)) + '\n')

# def read_file(file_name):
#     with open(str(file_name), 'r') as f:
#         s = f.read()
#         print(s)


def random_nos(count):
    with open('random_nos.txt', 'w+') as f:
        for n in range(1, count + 1):
            f.write(str(random.randint(100, 200)) + '\n')
        f.seek(0)
        print(f.read())

def main():
    random_nos(10)
    # read_file('random_nos.txt')

if __name__ == '__main__':
    main()
