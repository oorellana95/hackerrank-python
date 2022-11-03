#!/bin/python3

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def diagonal_difference(arr):
    sum_left_to_right = 0
    sum_right_to_left = 0

    index = 0
    for a in arr:
        sum_left_to_right += a[index]
        sum_right_to_left += a[len(arr) - index - 1]
        index += 1

    return abs(sum_left_to_right - sum_right_to_left)


if __name__ == '__main__':
    print(diagonal_difference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
