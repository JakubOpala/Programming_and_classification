import numpy as np
import math
import itertools
from itertools import chain, combinations

# 1st task --------------------------------------------------------------------------------------------------

"""
We ask the user for an input and make a number from it. Then we check if this number is an integer and if it is,
then we check if it is odd or even number.
"""


def even_odd():
    num = input("Type any number: ")
    if num.isnumeric() or (num[0] == '-' and num[1:].isnumeric()):
        num = float(num)
        if (num % 1 == 0):
            if num % 2 == 0:
                print("This number is even integer")
            else:
                print("This number is odd integer")
        else:
            print("This number is not an integer")
    else:
        print("This is not a number, try again:")
        even_odd()

even_odd()

# 2nd task --------------------------------------------------------------------------------------------------

"""
We generate array of 20 random integers from an interval 10 to 99 and we calculate mean of this set and we find
the maximal value.
"""

rand_arr = np.random.randint(10,99,20)

print("Generated array: ", rand_arr)

mean = np.mean(rand_arr)
max = np.max(rand_arr)

print("Mean value is equal: ", mean)
print("Maximum value is equal: ", max)

