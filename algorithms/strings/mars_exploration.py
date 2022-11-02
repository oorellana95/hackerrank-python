#!/bin/python3
import re


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def mars_exploration(s):
    number_sos = int(len(s) / 3)
    counter = 0
    for i in range(number_sos):
        if s[i*3] != "S":
            counter += 1
        if s[i*3+1] != "O":
            counter += 1
        if s[i*3+2] != "S":
            counter += 1
    return counter


if __name__ == '__main__':
    print(mars_exploration("SOSTOTPXP"))
