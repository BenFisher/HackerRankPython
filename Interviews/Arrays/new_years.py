# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

t0 = '''2
5
2 1 5 3 4
5
2 5 1 3 4  
'''

t1 = '''2
8
5 1 2 3 7 8 6 4
8
1 2 5 3 7 8 6 4'''

t2 = '''2
5
2 1 5 3 4
5
2 5 1 3 4'''

def minimumBribes(q):
    n = len(q)
    bribes = 0
    for i in range(n):
        q_i = q[i]
        if (q_i - i - 1) > 2:
            return "Too chaotic"
        for j in range(i,q_i-2,-1):
            bribes += (j>0) and (q[j-1] > q_i)
    return str(bribes)


if __name__ == '__main__':
    t = t1.splitlines()
    n=int(t[0])
    #t = int(test_in[0])
    q=[int(i) for i in '5 1 2 3 7 8 6 4'.split()]
    print(minimumBribes(q))
    #t = int(input())


    for t_itr in range(n):
        break
        #n = int(input())
        #q = list(map(int, input().rstrip().split()))
        
        n = int(t[t_itr*2+1])
        q = [int(i) for i in list(t[t_itr*2+2].split())]   
        print(minimumBribes(q)) 