
#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    altitude = 0
    in_valley = 0
    num_valleys = 0
    i=0
    for step in path:
        i+=1
        if step == 'U':
            altitude+=1
        elif step == 'D':
            altitude-=1
        print('step=' + str(i) + '|' + step + '|alt=' + str(altitude))
        if in_valley == 0 and altitude < 0:
            in_valley = 1
            print('\tStep ' + str(i) + " in valley")
        if in_valley == 1 and altitude == 0:
            in_valley = 0
            num_valleys += 1
            print('\tStep ' + str(i) + " leave valley")
        
    return num_valleys
        
        
