#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def frequency_query(queries):
    results = []
    data = {}
    for query in queries:
        command = query[0]
        number = query[1]
        if command == 1:
            if number in data:
                data[number] += 1
            else:
                data[number] = 1
        elif command == 2 and data.get(number):
            data[number] -= 1
        elif command == 3:
            # sum(value == number for value in data.values())
            results.append(1 if number in data.values() else 0)
    return results


if __name__ == '__main__':
    queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
    print(frequency_query(queries))
