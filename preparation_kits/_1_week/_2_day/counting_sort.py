import numpy as np
import time


def countingSortWithNumpy(arr):
    unique_values, counts = np.unique(arr, return_counts=True)
    frequency_array = np.zeros((100,), dtype=int)

    for i in range(len(unique_values)):
        frequency_array[unique_values[i]] = counts[i]

    print(*frequency_array)

def countingSort(arr):
    arr.sort()
    frequency_array = []
    pointer = 0
    for i in range(100):
        frequency_array.append(0)
        for j in range(pointer, len(arr)):
            if arr[j] == i:
                frequency_array[i] += 1
            else:
                pointer = j
                break

    print(*frequency_array)


if __name__ == '__main__':
    start = time.time()
    arr = [1, 2, 3, 4, 2, 1, 99]
    print(countingSort(arr))
    end = time.time()
    print(end - start)
