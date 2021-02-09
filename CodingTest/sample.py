#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzzTest(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizBuzz'
    if n % 3 == 0 and n % 5 != 0:
        return 'Fizz'
    if n % 3 != 0 and n % 5 == 0:
        return 'Buzz'
    return str(n)

def fizzBuzz(n):
    print(fizzBuzzTest(n))


if __name__ == '__main__':