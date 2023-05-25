import numpy as np
import itertools
import nltk
import re

# Assignment 24 ====================================================================================================


def hamming(a, b):

    """
    Function takes two strings of the same length and returns hamming distnce between them.

    Parameters:
            a[String] - first string
            b[String] - second string
    
    Return:
            dist[Int] - Hamming distance between a and b

    Conditions:
            a and b length must be the same

    """

    if (len(a) != len(b)):
        raise ValueError
    #diff_bits = [(int(a[i])+int(b[i])) % 2 for i in range(len(a))]
    diff_bits = [1 - int(a[i] == b[i]) for i in range(len(a))]
    dist = sum(diff_bits)
    return dist

def is_bitstring(string):

    """
    Function takes a string and checks if it is a bitstring

    Parameters:
            string[String] - string for check
    
    Return:
            is_bitstring[Bool] - True if string is bitstring and False otherwise
    """

    pattern = r'^[01]+$'
    is_bitstring = bool(re.match(pattern, string))
    return is_bitstring

def sim_bitstrings(b, n):

    """
    Function takes a string b and integer n and returns a set of strings that have Hamming distance
    from b equal to n.

    Parameters:
            b[String] - string
            n[Int] - Hamming distance for our set
    
    Return:
            similars[Set] - set of strings that have Hamming distance from b equal to n.

    Conditions:
            n must be not smaller than 0 and not bigger than length of b
    """

    if (n > len(b) or n < 0):   
        raise ValueError
    
    if (not is_bitstring(b)):
        raise AttributeError

    n_ones = hamming(b, '0' * len(b))

    ones = []
    zeros = []

    for k in range(len(b)):
        if b[k] == '1':
            ones.append(k)
        else:
            zeros.append(k)

    res = []

    for i in range(0,min([n,n_ones])+1):
        for perm1 in itertools.permutations(ones, i):
            for perm0 in itertools.permutations(zeros, n-i):
                sim = list(b)
                if i>0:
                    for x in perm1:
                        sim[x] = '0'
                if i<n:
                    for y in perm0:
                        sim[y] = '1'
                res.append("".join(sim))

    similars = set(res)
    return similars

# Assignment 25 ====================================================================================================

def set_jaccard(set1, set2):

    """
    Function takes two sets and returns jaccard similarity between them

    Parameters:
            set1[Set] - first set
            set2[Set] - second set
    
    Return:
            jaccard_similarity[Int] - jaccard similarity between set1 and set2

    Conditions:
            at least one of the sets must be nonempty
    """

    if len(set1) == 0 and len(set2) ==0:
        raise ValueError

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    jaccard_similarity = len(intersection) / len(union)
    return jaccard_similarity

# Assignment 26 =====================================================================================================

def bag_jaccard(x, y):

    """
    Function takes two sets and returns jaccard similarity between them

    Parameters:
            x[String] - first set
            y[String] - second set
    
    Return:
            jaccard_similarity[Int] - jaccard similarity between x and y

    Conditions:
            at least one of the strings must have nonzero length
    """

    if len(x) == 0 and len(y) == 0:
        raise ValueError

    bag1 = set(nltk.word_tokenize(x))
    bag2 = set(nltk.word_tokenize(y))

    intersection = bag1.intersection(bag2)
    union = bag1.union(bag2)

    jaccard_similarity = len(intersection) / len(union)
    return jaccard_similarity

# Assignment 27 =====================================================================================================

def shingles(s, k):

    """
    Function takes a string s and integer k and returns a set of all k-length shingles of s.

    Parameters:
            s[String] - string for shingling
            k[Int] - length of shingles
    
    Return:
            kshingles[Set] - set of all k-shingles of s

    Conditions:
            k must be greater than 0 and not bigger than len(s)
    """

    if len(s) < k or 0 > k:
        raise ValueError

    kshingles = set()

    for i in range(len(s)-k+1):
        kshingles.add(s[i:i+k])

    return kshingles

#string_for_shingle = "abcdefghij"
#print(shingles(string_for_shingle,3))

# Assignment 28 =====================================================================================================

def diameter(S, d):

    """
    Function takes a set of strings S and distance function d and returns a diameter of metric space (S, d).

    Parameters:
            S[Set[String]] - set of words
            d([String, String]) - distance function
    
    Return:
            diam[Int] - diameter od (S, d) metric space

    """

    diam = 0
 
    for pair in itertools.combinations(S, 2):
        len_diam = d(pair[0], pair[1])
        if len_diam > diam:
            print(pair[0], pair[1], len_diam)
            diam = len_diam

    return diam



''' not used
    string_dict = {}

    for strin in S:
        
        string_length = len(str(strin))
        
        if string_length not in string_dict:
            string_dict[string_length] = []
        
        string_dict[string_length].append(str(strin))
    
    string_dict = dict(sorted(string_dict.keys(), key=lambda x:x[1]), reverse = True)
    diam = 0

    for length, arr in string_dict.items():
        if diam > length:
            return diam
        len_diam = max([d(pair[0],pair[1]) for pair in itertools.permutations(arr, 2)])
        diam = max(len_diam, diam)

    #diam = max([d(pair[0],pair[1]) for pair in itertools.permutations(S, 2) if len(pair[0])==len(pair[1])])
    return diam

'''
