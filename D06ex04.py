#!/usr/bin/env python3
import random

def read_roster():
    with open('roster.txt', 'r') as f:
        line = f.readline()
        new_fin = open('new_roster.txt', 'w')
        count = 0
        for line in f:
            x = line.split()
            if len(x) == 3:
                if 'e' in x[0]+x[1] or 'E' in x[0]+x[1]:
                    print(x[0] + ' '+ x[1])
                    new_fin.write(x[0]+'\n')
                    count += 1
            else:
                if 'e' in x[0] or 'E' in x[0]:
                    print(x[0])
                    new_fin.write(x[0]+'\n')
                    count += 1


    print("Total number of names that contain letter 'e' : {}".format(count))
    new_fin.write("Total number of names that contain letter 'e' : {}".format(count))
    new_fin.close()


# def read_roster():
#     with open('roster.txt', 'r') as f:
#         line = f.readline()
#         new_fin = open('new_roster.txt', 'w')
#         count = 0
#         for line in f:
#             x = line.split()
#             if 'e' in x[0]:
#                 print(x[0])
#                 new_fin.write(x[0]+'\n')
#                 count += 1

#     print("Total number of names that contain letter 'e' : {}".format(count))
#     new_fin.write("Total number of names that contain letter 'e' : {}".format(count))
#     new_fin.close()


def main():
    
    read_roster()

if __name__ == '__main__':
    main()
