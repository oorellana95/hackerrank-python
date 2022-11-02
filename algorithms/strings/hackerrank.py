#!/bin/python3
import re


#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrank_in_string(s):
    sequence = "hackerrank"
    substring = s
    for c in sequence:
        try:
            substring = substring[substring.index(c)+1:]
        except ValueError:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    print(hackerrank_in_string("hackerraaaankkkk"))
