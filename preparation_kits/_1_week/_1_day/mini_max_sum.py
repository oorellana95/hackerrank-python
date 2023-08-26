import time



def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[0:-1])
    max_sum = sum(arr[1:])
    print(f"{min_sum} {max_sum}")


if __name__ == '__main__':
    start = time.time()
    arr = [1, 4, 5, 7, 3]
    miniMaxSum(arr)
    end = time.time()
    print(end - start)
