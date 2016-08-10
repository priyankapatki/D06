#!/usr/bin/env python3
import random


def read_roster():
    with open('roster.txt', 'r') as f:
        line = f.readline()
        count = 0
        for line in f:
            x = line.split()
            if len(x) == 3:
                if 'e' in x[0]+x[1] or 'E' in x[0]+x[1]:
                    print(x[0] + ' '+ x[1])
                    count += 1
            else:
                if 'e' in x[0] or 'E' in x[0]:
                    print(x[0])
                    count += 1


    print("Total number of names that contain letter 'e' : {}".format(count))


def main():
    
    read_roster()

if __name__ == '__main__':
    main()
