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


if __name__ == '__main__':

    t = 4
    _input = ["{[()]}", "{[(])}", "{{[[(())]]}}", "{(([])[])[]}"]
    for t_itr in range(t):
        s = _input[t_itr]

        result = isBalancedWeak(s)

        print(result)
