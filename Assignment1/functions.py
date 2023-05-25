import numpy as np
import math
import itertools
from itertools import chain, combinations
from collections import Counter
import pandas as pd

# 3rd task ---------------------------------------------------------------------------------------------------

def cosine(v1, v2):
    
    """
    Function takes as arguments 2 n-dimensional vectors and returns cosinus of an angle between 
    them by calculating their scalar product and dividing it by their lengths.

    Parameters:
            v1(Array[float]): vector
            v2(Array[float]): vector with the same numbers of elements as v1

    Return:
            cos(float): cosine of the angle between v1 and v2

    Conditions:
            -v1 and v2 must have the same dimensions (number of elements)
    """

    scalar_product = np.dot(v1, v2)
    l1 = np.linalg.norm(v1)
    l2 = np.linalg.norm(v2)
    if l1 == 0 or l2 ==0:
        raise ValueError("vector(s) with 0 length given")
    cos = scalar_product/(l1*l2)
    return cos

# 4th task ---------------------------------------------------------------------------------------------------

def divisible_in_range(a, b, d):

    """
    Function takes a set of integers, noted by its first a and last b elements and another integer d
    and returns a list of integers a<x<b that are divisible by d. 
    
    Parameters:
            a(Int): lower boundary of our set of integers (not in set)
            b(Int): upper boundary of our set of integers (not in set)
            d(Int): divisor of the numbers that we are searching for

    Return:
            divisors(Array[Int]): set of integers bigger than a and lower than b, that are divisible by d

    Conditions:
            - a < b-1 , otherwise our set is empty
            - d < b , otherwise
    """

    divisors = np.array([])

    if a > b:
        raise ValueError('a(lower boundary of set) is bigger than b(upper boundary)')
    if d > a:
        a = d
    if d > b-1:
        raise ValueError('d is bigger than the biggest number in set')
        print("Given divisor is bigger than the biggest integer in set - no divisors")
    else:
        for i in range(a+1,b):
            if i % d == 0:
                divisors = np.append(divisors, i)
    
    return list(divisors)

# 5th task ---------------------------------------------------------------------------------------------------

def common_elements(x, y):

    """
    Function takes two lists x and y, then returns a list their common elements.

        Parameters:
                x(List[Any]): list of any elements
                y(List[Any]): list of any elements

        Return:
                common(List[Any]): list of common elements of x and y
                
    """

    common = np.array([])   
    a = np.size(x)
    b = np.size(y)
    i = 0
    j = 0

    while(i<a):
        while(j<b):
            if type(x[i]) == type(y[j]):
                if x[i] == y[j]:
                    common = np.append(common,x[i]) 
                    x = np.delete(x, i)
                    y = np.delete(y, j)
                    a = a-1
                    b = b-1
                    i -= 1
                    j -= 1
            j += 1
        j = 0
        i += 1

    return common

# 6th task ---------------------------------------------------------------------------------------------------

def exclude(letter, string):

    """
    Function takes a character and deletes all its occurences in a given string.

    Parameters:
            letter(Char): character to be deleted from string
            string(String): string for performing character removal
        
    Return:
            removed(String): string given at the beginning with every occurence of given character deleted

    """
    letter = str(letter)
    string = str(string)
    removed = string.replace(letter, '')
    return removed

# 7th task ---------------------------------------------------------------------------------------------------

def letters_and_digits(s):

    """
    Function takes a string and returns a 2-element list. First element of this list is a number of
    letters in given string and the second element denotes number of digits.

    Parameters:
            s(String): string in which we will count letters and digits

    Return:
            counts([Int, Int]): 2-element list with number of letters in given string in first position
            and number of digits in second position
    """

    n_let = 0
    n_dig = 0
    for i in s:
        if i.isalpha():
            n_let += 1
        elif i.isdigit():
            n_dig += 1
    counts = [n_let, n_dig]
    return counts

# 8th task ---------------------------------------------------------------------------------------------------

def subsets(x):

    """
    Function takes a set and returns every possible subset.

    Parameters:
            x(set[Any]): given set
    
    Return:
            subs(set(Any)): set consisting of tuples with every possible subset of x, including an empty set
    """
    if not(isinstance(x,list)):
        raise TypeError("input is not a list")
    a = set(x)
    subs = []
    for i in range(len(a)+1):
        subs += combinations(a,i)
    return subs

# 9th task ---------------------------------------------------------------------------------------------------


def mode(s):

    """
    Function takes a single string and returns a list of most common letters in it.

    Parameters:
            s(String): any string

    Returns:
            most_common(List(Char)): list of most common letters in s
    """

    char_count = Counter(s)
    most_common = char_count.most_common()
    most_common = [char for char, count in most_common if (count == most_common[0][1] and char.isalpha())]
    return most_common

# 10th task ---------------------------------------------------------------------------------------------------

def dec_to_bin(x):

    """
    Function takes an integer - decimal representation of number as input and returns its representation in
    binary system in a form of string.

    Parameters:
            x(Int): number to convert

    Returns:
            x_bin(String): string representing binary representation of x
    """
    x_bin = bin(x)
    return x_bin


# 11th task ---------------------------------------------------------------------------------------------------

def non_negative(x):

    """
    Function takes a list of numbers as input and returns it with all negative numbers removed.

    Parameters:
            x(List[Float]): initial list

    Returns:
            non_negative(List[Float]): x with all negative numbers removed
    """
    non_negative = [i for i in x if i > 0]
    return non_negative


# 12th task ---------------------------------------------------------------------------------------------------

def no_longer_than(threshold, x):

    """
    Function takes an integer - threshold and list of strings and return it with all strings longer
    than threshold removed.

    Parameters:
            threshold(Int): defines the maximal length of strings in returned array
            x(List[String]): initial list

    Returns:
            new_arr(List[String]):  x with all strings longer than threshold removed

    Conditions:
            threshold must not be less than 0
    """

    if threshold < 0:
        raise ValueError('threshold cant be a negative number')
    new_arr = [string for string in x if len(string) <= threshold]
    return new_arr

# 13th task ---------------------------------------------------------------------------------------------------

def max_string(x):

    """
    Function takes a list of strings and returns a list consisting of the longest strings from it.

    Parameters:
            x(List(String)): initial array of strings

    Returns:
            max_str(List(String)): array consisting of the longest strings from x
    """

    str_leng = [len(string) for string in x]
    max_len = np.amax(str_leng)
    max_str = [string for string in x if len(string) == max_len]
    return max_str

# 14th task ---------------------------------------------------------------------------------------------------

import itertools

def alternate(a, b):

    """
    Function takes two lists: a and b, and constructs a list that keeps alternately consecutive elements from
    a and b.

    Parameters:
            a(List(Any)): first list for alternating
            b(List(Any)): second list for alternating

    Returns:
            alternated(List(Any)): alternately merged lists a and b

    Conditions:
            length of an array a must be the same as the length of an array b
    """

    if len(a) != len(b):
        raise ValueError("lists have different lengths")
    list = itertools.chain.from_iterable(itertools.zip_longest(a,b))
    alternated = [x for x in list]
    return alternated

# 15th task ---------------------------------------------------------------------------------------------------

def separate_and_sort(x):

    """
    Function takes an array of integers and strings nd returns an array starting with strings in alphabetical order,
    followed by sorted in increasing order integers.

    Parameters:
            x(Array(Any)): for separating and sorting

    Returns:
            sorted(Array(Any)): separated and sorted array
    """

    letters = [i for i in x if str(i).isalpha()]
    numbers = [i for i in x if str(i).isdigit()]
    x1 = np.sort(letters, kind='mergesort')
    x2 = np.sort(numbers, kind='mergesort')
    sorted = np.append(x1,x2)
    return sorted
