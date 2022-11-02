#!/bin/python3
from collections import Counter


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    length = len(s)
    if length % 2 != 0:
        return -1

    half_length = int(length / 2)
    first_word = list(s[0:half_length])
    second_word = list(s[half_length:])
    mismatch = Counter(first_word) - Counter(second_word)
    return sum(mismatch.values())


if __name__ == '__main__':
    print(anagram("mapaaaaa"))
