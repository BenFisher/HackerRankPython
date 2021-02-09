#!/bin/python3
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
import math

def nextCloud(c, clouds):
    if c < len(clouds) - 2 and int(clouds[c+2]) == 0:
        return c+2
    return c+1
    
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(clouds):
    c_end = len(clouds)
    jumps = 0
    c = 0
    while c < c_end-1:
        c = nextCloud(c, clouds)
        print(c)
        jumps+=1
    return jumps

t='0 0 1 0 0 1 0'

print(jumpingOnClouds(t.split()))