import time


def diagonalDifference(arr):
    sum_left_to_right_diagonal, sum_right_to_left_diagonal = 0, 0
    size = len(arr)
    for i in range(size):
        sum_left_to_right_diagonal += arr[i][i]
        sum_right_to_left_diagonal += arr[i][size-1-i]
    return abs(sum_left_to_right_diagonal-sum_right_to_left_diagonal)


if __name__ == '__main__':
    start = time.time()
    arr = [[1, 1, 2],
           [2, 3, 3],
           [4, 1, -3]]
    print(diagonalDifference(arr))
    end = time.time()
    print(end - start)
