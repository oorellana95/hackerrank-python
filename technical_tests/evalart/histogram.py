#!/bin/python3
from typing import List


def solution(myArray: List[int]):
    for i in range(1, 6):
        asterisks = "*" * myArray.count(i)
        print(f"{i}: {asterisks}")


if __name__ == '__main__':
    a = [1, 1, 4, 5, 3]
    solution(a)

