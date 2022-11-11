#!/bin/python3

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compare_triplets(a, b):
    first, second = 0, 0
    for i in range(3):
        first += 1 if a[i] > b[i] else 0
        second += 1 if a[i] < b[i] else 0
    return [first, second]


if __name__ == '__main__':
    a = [4, 4, 1]
    b = [3, 4, 2]
    print(compare_triplets(a, b))
