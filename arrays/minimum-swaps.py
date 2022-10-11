#!/bin/python3
from typing import List


# Complete the minimumSwaps function below.
def minimum_swaps(arr: List[int]):
    count = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            count += 1
    return count


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 6, 7]
    print(minimum_swaps(arr=arr))
