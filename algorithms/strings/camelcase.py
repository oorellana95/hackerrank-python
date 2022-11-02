#!/bin/python3
from collections import Counter


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1


if __name__ == '__main__':
    print(camelcase("mapaaaaaSa"))
