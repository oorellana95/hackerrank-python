import numpy as np


def pairs(k, arr):
    arr.sort(reverse=True)
    result_arr = []
    for i in arr:
        result_arr.append(i - k)

    pairs = len(list(np.intersect1d(arr, result_arr)))
    print(pairs)


if __name__ == '__main__':
    pairs(1, [1, 2, 3, 4])
