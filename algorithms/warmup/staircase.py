#!/bin/python3
from typing import List


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def staircase(n):
    for i in range(n):
        hashes = (i+1)*'#'
        print(hashes.rjust(n, ' '))



if __name__ == '__main__':
    n = 6
    staircase(n=n)
