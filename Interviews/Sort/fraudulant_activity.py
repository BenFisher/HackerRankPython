#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

def insert(list, n): 
    bisect.insort(list, n)  
    return list

def findMedian(e_list):
    d=len(e_list)
    idx = int(d/2)
    if d % 2:
        return int(e_list[idx])
    else:
        return int(e_list[idx - 1] + e_list[idx]) / 2

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    spend_list = [(int(i)) for i in expenditure[0:d]]
    spend_list.sort()
    alerts = 0
    for i in range(d,len(expenditure)):
        e=int(expenditure[i])
        e_med = findMedian(spend_list)
        if e >= e_med*2:
            alerts += 1
            #spend_list = insert(spend_list, e)
        e_first = int(expenditure[i-d])
        spend_list.remove(e_first)
        spend_list = insert(spend_list, e)
        #print(str(i))
    print(alerts)

# t1 answer is 633
t1 = 'Interviews/Sort/fraud_test_t1.dat'

if __name__ == '__main__':
    f = open(t1, 'r')
    t = f.readlines()
    d = int(t[0].split()[1])
    e = t[1].split()
    activityNotifications(e, d)