#!/bin/python3

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangram(s):
    alphabet_lowercase = set("abcdefghijklmnopqrstuvwxyz")
    string_lowercase = set(s.lower())
    difference = alphabet_lowercase - string_lowercase
    return 'pangram' if len(difference) == 0 else 'not pangram'


if __name__ == '__main__':
    print(pangram("We promptly judged antique ivory buckles for the next prize"))
