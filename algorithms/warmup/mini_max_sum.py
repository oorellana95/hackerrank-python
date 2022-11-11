#!/bin/python3
from typing import List


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plus_minus(arr: List[int]):
    sum_array = sum(arr)
    first_output = sum_array - max(arr)
    second_output = sum_array - min(arr)
    print(first_output, second_output)


if __name__ == '__main__':
    arr = [3, 5, 6, 7, 8]
    plus_minus(arr=arr)
