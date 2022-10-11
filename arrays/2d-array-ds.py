#!/bin/python3
from typing import List


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglass_sum(arr: List[List[int]]):
    maximum_hourglass_sum = None
    for i in range(4):
        for j in range(4):
            single_hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                                   arr[i+1][j+1] + \
                                   arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if maximum_hourglass_sum is None or single_hourglass_sum > maximum_hourglass_sum:
                maximum_hourglass_sum = single_hourglass_sum

    return maximum_hourglass_sum


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print(hourglass_sum(arr=arr))
