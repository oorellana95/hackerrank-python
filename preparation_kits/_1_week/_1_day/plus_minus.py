import time
import numpy as np


# For large arrays is better this approach (example 10.000 numbers)
def plusMinusBigArrays(arr):
    np_arr = np.array([0, 0, 0])
    size = len(arr)
    for i in range(size):
        if arr[i] > 0:
            np_arr[0] += 1
        elif arr[i] < 0:
            np_arr[1] += 1
        else:
            np_arr[2] += 2
    np_arr = np_arr/size

    print(f'{np_arr[0]}\n'
          f'{np_arr[1]}\n'
          f'{np_arr[2]}')


# For the problem is much better this approach since max. n=100
def plusMinus(arr):
    positive, negative, zero = 0, 0, 0
    size = len(arr)
    for i in range(size):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1
    print(f'{positive/size}\n'
          f'{negative/size}\n'
          f'{zero/size}')


if __name__ == '__main__':
    start = time.time()
    arr = [-5, -3, 1, 0, -5, -3, 1, 0, -5, -3, 1, 0]
    plusMinus(arr)
    end = time.time()
    print(end - start)
