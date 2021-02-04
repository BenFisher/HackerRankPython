#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

array = '''1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0'''

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hg_size = len(arr[0]) - 2
#    hg_sums = []
#    hg_sums_array = []
    max_sum = None
    for i in range(1, hg_size+1):
        for j in range(1, hg_size+1):
            hg = [arr[i-1][j-1:j+2], [arr[i][j]], arr[i+1][j-1:j+2]]
            hg_sum = sum(sum(hg,[]))
            if max_sum == None:
                max_sum = hg_sum
            else:
                max_sum = hg_sum if hg_sum > max_sum else max_sum
        #    hg_sums.append(hg_sum)
        #hg_sums_array.append(hg_sums)
        #hg_sums = []
        #print(hg_sums_array)
    return max_sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []
    array_lines = array.splitlines()
    for i in range(6):
        arr.append(list(map(int,array_lines[i].split())))
        #arr.append(list(map(int, input().rstrip().split())))

    #print(arr)
    result = hourglassSum(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
