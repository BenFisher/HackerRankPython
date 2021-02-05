
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    num_toys = 0
    sum_prices = 0
    max_p = 0
    toys = []
    for i in range(len(prices)):
        p = prices[i]
        # Check if adding p stays under k
        if sum_prices + p < k:
            sum_prices += p
            num_toys += 1
            toys.append(p)
            # Change max_p if this is the biggest price
            if p > max_p:
                max_p = p
        # If and only if p brings the sum over k
        # but switching p for max_p does not, do so
        elif sum_prices - max_p + p < k:
            toys.remove(max_p)
            toys.append(p)
            sum_prices -= max_p
            sum_prices += p
            if p > second_p:
                max_p = p
    toys.sort()
    print(toys)
    print(sum(toys))
    return num_toys

t1 = '''7 50
1 12 5 111 200 1000 10 2 18 17 1 3 4 '''
if __name__ == '__main__':
    #t = t1.splitlines()
    f = open('Interviews/Sort/mark_and_toys_t1.dat', 'r')
    t=f.readlines()
    k=int(t[0].split()[1])
    prices=[int(i) for i in t[1].split()]

    result = maximumToys(prices, k)
    print(result)