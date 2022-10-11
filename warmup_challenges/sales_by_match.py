#!/bin/python3
import math
from typing import List


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sock_merchant(n: int, ar: List[int]):
    socks_dict = {}
    for i in ar:
        sock_item = socks_dict.get(i)
        if sock_item is not None:
            socks_dict[i] = sock_item + 1
        else:
            socks_dict[i] = 1

    pairs = 0
    for k in socks_dict.keys():
        pairs = pairs + math.trunc(socks_dict[k] / 2)

    return pairs


if __name__ == '__main__':
    n = 7
    ar = [1, 2, 1, 2, 1, 3, 2, 3]
    print(sock_merchant(n=n, ar=ar))
