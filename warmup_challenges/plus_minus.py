#!/bin/python3
from typing import List


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plus_minus(arr: List[int]):
    q_positive, q_negative, q_zeros = 0, 0, 0

    for a in arr:
        if a > 0:
            q_positive += 1
        elif a < 0:
            q_negative += 1
        else:
            q_zeros += 1

    def print_division(num_1: int, num_2: int):
        print(format(num_1/num_2, '.6f'))

    print_division(q_positive, len(arr))
    print_division(q_negative, len(arr))
    print_division(q_zeros, len(arr))


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plus_minus(arr=arr)
