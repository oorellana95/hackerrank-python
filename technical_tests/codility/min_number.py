#!/bin/python3
from typing import List


def solution(A: List[int]):
    _set = set(A)
    response = 1
    while response in _set:
        response += 1
    return response


if __name__ == '__main__':
    a = [1, 3, 6, 4, 1, 2]
    print(solution(a))
