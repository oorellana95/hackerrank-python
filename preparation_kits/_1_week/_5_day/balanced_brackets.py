#!/bin/python3

import os

def isBalancedWeak(s):
    s_len = len(s)
    if s_len % 2 != 0:
        "NO"

    my_bracket_dict = {"[": "]", "(": ")", "{": "}"}

    for i in range(s_len // 2):
        if my_bracket_dict.get(s[i]) == s[s_len - (i+1)]:
            pass
        else:
            return "NO"
    return "YES"


def isBalanced(s):
    if len(s) % 2 != 0:
        "NO"

    previous_length = 0
    while previous_length != len(s):
        previous_length = len(s)
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        s = s.replace('()', '')

    return "YES" if len(s) == 0 else "NO"


if __name__ == '__main__':

    t = 4
    _input = ["{[()]}", "{[(])}", "{{[[(())]]}}", "{(([])[])[]}"]
    for t_itr in range(t):
        s = _input[t_itr]

        result = isBalanced(s)

        print(result)
