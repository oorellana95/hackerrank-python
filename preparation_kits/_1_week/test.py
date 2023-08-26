import time


def findMedian(arr):
    arr.sort()
    median_position = len(arr) // 2
    return arr[median_position]


if __name__ == '__main__':
    start = time.time()
    arr = [0, 1, 2, 4, 6, 5, 3]
    print(findMedian(arr))
    end = time.time()
    print(end - start)
