#!/bin/python3
from collections import Counter
import re

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

"""
Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
"""


def strong_password(password):
    def missing(pattern: str):
        if len(re.findall(pattern, password)) == 0:
            return 1
        return 0

    min_number_characters = 0
    min_number_characters += missing(r'[A-Z]')
    min_number_characters += missing(r'[a-z]')
    min_number_characters += missing(r'[0-9]')
    min_number_characters += missing(r'[!@#$%^&*()\-+]')

    if (len(password) + min_number_characters) < 6:
        min_number_characters = 6 - len(password)

    return min_number_characters


if __name__ == '__main__':
    print(strong_password("abcdw9"))
