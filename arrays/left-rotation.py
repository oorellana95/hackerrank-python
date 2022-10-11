#!/bin/python3
import math
from typing import List


#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rot_left(a: List[int], d: int):
    return a[d:len(a)] + a[0:d]


if __name__ == '__main__':
    d = 10
    # a = [1, 2, 3, 4, 5]
    a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
    print(rot_left(a=a, d=d))
