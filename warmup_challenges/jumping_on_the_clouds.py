#!/bin/python3
from typing import List


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumping_on_clouds(c: List[int]):
    while_condition = len(c) - 1
    total_jumps = 0
    i = 0
    while i < while_condition:
        if (i + 2) <= while_condition and c[i + 2] == 0:
            i = i + 2
        elif c[i + 1] == 0:
            i = i + 1
        total_jumps = total_jumps + 1

    return total_jumps


if __name__ == '__main__':
    # c = [0, 0, 1, 0, 0, 1, 0]
    c = [0, 0, 0, 1, 0, 0]
    print(jumping_on_clouds(c=c))
