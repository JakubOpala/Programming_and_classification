import nltk
import numpy as np
import itertools

def gen_hash(m):

    def hash_fun(bitstring):
        integ = int(bitstring, 2)
        arr = [int(dig) for dig in str(integ)]
        hash_value = sum([val % m for val in arr]) % m
        return hash_value
    
    return hash_fun
    

bitstring = "01100111"
hash_fun = gen_hash(len(bitstring))
hash = hash_fun(bitstring)
print(hash)
print(int("111",2))
