#!/bin/python3
from collections import defaultdict


#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


# Complete the count triplets function below.
"""def count_triplets(arr: List[int], r: int):
    dic = {}
    counter = 0
    arr.sort()
    
    for value in arr:
        if dic.get(value) is None:
            dic[value] = 1
        else:
            dic[value] += 1

    for i in range(len(dic)-2):
        items = [dic.get(r ** i), dic.get(r ** (i + 1)), dic.get(r ** (i + 2))]
        is_there_none = any(item is None for item in items)
        counter += 0 if is_there_none else math.prod(items)

    return counter"""


"""def count_triplets(arr: List[int], r: int):
    dic = dict((x, arr.count(x)) for x in set(arr))
    counter = 0
    for i in range(len(dic)-2):
        first_item_triplet = dic.get(r ** i)
        if first_item_triplet is not None:
            second_item_triplet = dic.get(r ** (i+1))
            if second_item_triplet is not None:
                third_item_triplet = dic.get(r ** (i + 2))
                if third_item_triplet is not None:
                    counter += first_item_triplet * second_item_triplet * third_item_triplet

    return counter"""

"""def countTriplets(arr, r):
        # initialize the dictionaries
        r2 = {}
        r3 = {}
        count = 0

        # loop throgh the arr items
        for k in arr:
                # if k in r3 indicates the triplet already completed,
                # the count need be incremented
                if k in r3:
                        count += r3[k]

                # if k in r2, it is the secound number of the triplet,
                # your successor (third element k*r) need be added or incremented in the r3 dict
                # because is a potencial triplet 
                if k in r2:
                        if k*r in r3:
                                r3[k*r] += r2[k]
                        else:
                                r3[k*r] = r2[k]

                # else, k is the first element of the triplet, so,
                # your seccessor (secound element k*r) need be added or incremented in the r2 dict
                # because is a potencial triplet
                if k*r in r2:
                        r2[k*r] += 1
                else:
                        r2[k*r] = 1

        return count"""


def count_triplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count


if __name__ == '__main__':
    arr = [1, 3, 9, 9, 27, 81]
    r = 3
    print(count_triplets(arr=arr, r=r))
