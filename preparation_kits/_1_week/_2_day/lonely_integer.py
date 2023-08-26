import time


def lonelyinteger(a):
    a.sort()
    position_last_element = len(a)-1
    for i in range(0, position_last_element, 2):
        if a[i] != a[i+1]:
            return a[i]
    return a[position_last_element]


if __name__ == '__main__':
    start = time.time()
    arr = [1, 1, 2, 2, 3, 3, 4]
    print(lonelyinteger(arr))
    end = time.time()
    print(end - start)
