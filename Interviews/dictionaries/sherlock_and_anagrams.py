import math
import os
import random
import re
import sys

# Create all possible substrings. Recurse from 1 to N-1 to create substring maps.
# Shift left to right to get all substrings, sort them, and add them to a dictionary
# When done, use items() on the hash map and look for the max num pairs 5->4 = 2 (no)
# Note - Do the anagrams have to be distinct? That gets annoying. They do not

# For a substring len substr_len, find all substrings and their pairs
def find_maps(s, substr_len, n_pairs):
    s_dict = {}
    pairs = 0
    for i in range(0, len(s) + 1 - substr_len):
        substr = "".join(sorted(s[i:i+substr_len]))
        
        try:
            s_dict[substr] += 1
        except KeyError:
            s_dict[substr] = 1
    
    for item in s_dict.items():
        n=item[1]
        pairs += n*(n-1)/2
         
    #print(s_dict)
    #print(pairs)

    if substr_len < len(s) - 1:
       pairs += find_maps(s, substr_len + 1, pairs)
    
    return pairs
    

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    pairs = find_maps(s, 1, 0)
    print(int(pairs))


sherlockAndAnagrams('ifailuhkqq')

