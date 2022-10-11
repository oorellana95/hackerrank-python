#!/bin/python3
import math

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeated_string(s: str, n: int):
    times = math.trunc(n / len(s))
    residual = n % len(s)

    if residual == 0:
        return s.count('a') * times
    else:
        return s.count('a') * times + s[0:residual].count('a')


if __name__ == '__main__':
    s = "ast"
    n = 10
    print(repeated_string(s=s, n=n))
