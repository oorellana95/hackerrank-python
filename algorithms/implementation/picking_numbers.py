#!/bin/python3
from collections import Counter


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def picking_numbers(arr):
    arr.sort()
    max_counter = 0
    for n in arr:
        value = arr.count(n) + arr.count(n + 1)
        if max_counter < value:
            max_counter = value
    return max_counter


if __name__ == '__main__':
    print(picking_numbers([1, 1, 2, 3, 4, 10, 11, 12]))
