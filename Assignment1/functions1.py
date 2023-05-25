import numpy as np
import math
import itertools
from itertools import chain, combinations

# 3rd task ---------------------------------------------------------------------------------------------------

def cosine(v1, v2):

    '''
    Function takes as arguments 2 n-dimensional vectors (v1,v2: Array[Float]) - so two arrays of float numbers
    and returns cosinus of an angle between them by calculating their scalar product and dividing
    it by their lengths.

    Conditions:
    -vectors must have the same dimensions (number of elements)
    '''

    scalar_product = np.dot(v1, v2)
    l1 = np.linalg.norm(v1)
    l2 = np.linalg.norm(v2)
    cos = scalar_product/(l1*l2)
    return cos


print("cosinus:", cosine([100,0],[1,1]))

# 4th task ---------------------------------------------------------------------------------------------------

def divisible_in_range(a, b, d):

    '''
    Function takes a set of integers, noted by its first (a:Int) and last (b:Int) elements and another integer (d:Int)
    and returns a list of integers a<x<b that are divisible by d. 
    If there is 
    '''


    divisors = np.array([0])

    if d > a:
        a = d
        if d > b:
            print("Given divisor is bigger than the biggest integer in set - no divisors")
            return divisors

    for i in range(a+1,b):
        if i % d == 0:
            divisors = np.append(divisors, i)
    
    return np.delete(divisors, 0)

print(divisible_in_range(10,14,9))

# 5th task ---------------------------------------------------------------------------------------------------

def common_elements(x, y):

    common = np.array([0])
    a = np.size(x)
    b = np.size(y)
    i = 0
    j = 0

    while(i<a):
        while(j<b):
            if type(x[i]) == type(y[j]):
                if x[i] == y[j]:
                    common = np.append(common, x[i])
                    x = np.delete(x, i)
                    y = np.delete(y, j)
                    a = a-1
                    b = b-1
                    i -= 1
                    j -= 1
            j += 1
        j = 0
        i += 1

    common = np.delete(common, 0)
    return common

print("Common element of given lists: ", common_elements(["a",1,2.5,5,5,5,3,"a",3,6],[5,3,"a"]))

# 6th task ---------------------------------------------------------------------------------------------------

def exclude(letter, string):
   
    string = string.replace(letter, '')
    return string


letter = input("Type a character you want to remove: ")
string = input("Type a string for character removal: ")
print(exclude(letter, string))

# 7th task ---------------------------------------------------------------------------------------------------

def letters_and_digits(s):
    n_let = 0
    n_dig = 0
    for i in s:
        if i.isalpha():
            n_let += 1
        elif i.isdigit():
            n_dig += 1
    return [n_let, n_dig]

string = input("Type a string to calculate number of letters and digits: ")
count = letters_and_digits(string)
print("Number of letters: ", count[0], ", number of digits: ", count[1])

# 8th task ---------------------------------------------------------------------------------------------------

def subsets(x):
    a = list(x)
    i = 0
    return chain.from_iterable(combinations(a, i) for i in range(len(a)+1))
    
print(list(subsets([1,2,3,"a"])))

# 9th task ---------------------------------------------------------------------------------------------------

from collections import Counter
import pandas as pd

def mode(s):
    char_count = Counter(s)
    most_common = char_count.most_common()
    return [char for char, count in most_common if count == most_common[0][1]]


most_common_elements = mode(input("Type a string to find most common letter: "))
print("Element(s) with most occurences: ", most_common_elements)
#print("Element(s) with most occurences: ", mode([1,"a","a",2,2,2,1,"a","a",1]))

# 10th task ---------------------------------------------------------------------------------------------------

def dec_to_bin(x):
    return bin(x)

number_to_bin = int(input("Type a number to convert to binary: "))
print("Binary representation: ", dec_to_bin(number_to_bin))

# 11th task ---------------------------------------------------------------------------------------------------

def non_negative(x):
    return [i for i in x if i > 0]

arr = [1,2,-5,4,-3,-2.5,2.1]
print("Array before non_negative application: ", arr, "\n and after: ", non_negative(arr))

# 12th task ---------------------------------------------------------------------------------------------------

def no_longer_than(threshold, x):
    return [string for string in x if len(string) <= threshold]

str_array = ["zibidibi", "2morrow", "hey", "s", "nice", "kamehameha"]
threshold = int(input("Type a number fot threshold: "))
print("Reduced string array: ", no_longer_than(threshold, str_array))

# 13th task ---------------------------------------------------------------------------------------------------

def max_string(x):
    str_leng = [len(string) for string in x]
    max_len = np.amax(str_leng)
    return [string for string in x if len(string) == max_len]

print("Longest string in array: ", max_string(str_array))



# 14th task ---------------------------------------------------------------------------------------------------

import itertools

def alternate(a, b):
    list = itertools.chain.from_iterable(itertools.zip_longest(a,b))
    return [x for x in list]

list1 = ["a1","a2","a3"]
list2 = ["b1","b2","b3"]
print(alternate(list1,list2))

# 15th task ---------------------------------------------------------------------------------------------------

def separate_and_sort(x):
    letters = [i for i in x if str(i).isalpha()]
    numbers = [i for i in x if str(i).isdigit()]
    x1 = np.sort(letters, kind='mergesort')
    x2 = np.sort(numbers, kind='mergesort')
    
    return np.append(x1,x2)

print(separate_and_sort(["f",5,2,"s","a",1,9,3]))