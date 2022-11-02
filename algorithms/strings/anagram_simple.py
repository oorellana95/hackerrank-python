#!/bin/python3

#
# Complete the 'anagram' function below.
#

def anagram(s1, s2):
    if len(s1) != len(s2):
        print("Invalid input")

    s1_list = list(s1)
    s2_list = list(s2)

    if s1_list.sort() == s2_list.sort():
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    anagram("india", "ndiia")
