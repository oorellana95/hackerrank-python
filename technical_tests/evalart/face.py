#!/bin/python3
from typing import List


def solution(n: int):
    base = "_" * n
    for i in range(n):
        row = base
        row = row[:i] + "X" + row[i + 1:]
        row = row[:n - i - 1] + "X" + row[n - i:]
        print(row)


if __name__ == '__main__':
    n = 7
    solution(n)
