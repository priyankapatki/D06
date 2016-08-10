#!/usr/bin/env python3
# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 4, [3]] # == 8
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(input_list):
    final_list =[]

    def single_list(input_list):
        list_length = len(input_list)
        
        for count in range(0, list_length):
            if 'int' in str(type(input_list[count])):
                final_list.append(input_list[count])

            else:
                single_list(input_list[count])
        return final_list
    single_list(input_list)
#    print("final_list : {}".format(final_list))
        
    total = sum(final_list)
    return total
    #print(" The sum of the list : {} = {}".format(input_list,repr(total)))
    

def main():
    ...
    #print(nested_sum([1, 4, [1, [4,0]]]))

if __name__ == '__main__':

    main()






