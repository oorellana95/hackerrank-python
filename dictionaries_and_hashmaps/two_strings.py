#!/bin/python3
from typing import List


#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def two_strings(s1: str, s2: str):
    s1_set = set(s1)
    s2_set = set(s2)
    intersection = s1_set.intersection(s2_set)
    return 'YES' if len(intersection) > 0 else 'NO'


if __name__ == '__main__':
    d = 10
    s1 = "be"
    s2 = "cat"
    print(two_strings(s1=s1, s2=s2))
