#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    arr = []
    while l <= r:
        if l%2 == 1:
            arr.append(l)
        l += 1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = oddNumbers(l, r)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()






    while i > arr[0]:
        if i == 1:
            anw.append(0)
            i += 1
        else:
            temp = 0
            temp = abs(arr[i]-arr[i-1])