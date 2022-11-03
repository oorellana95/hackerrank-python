#!/bin/python3
from collections import Counter


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def utopian_tree(n):
    tall = 1
    for i in range(0, n):
        if i % 2:
            tall += 1
        else:
            tall = tall * 2
    return tall


if __name__ == '__main__':
    print(utopian_tree(0))
