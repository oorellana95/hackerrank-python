#!/bin/python3

#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#


def findSum(numbers, queries):
    output = []
    for query in queries:
        op_numbers = numbers[(query[0]-1):query[1]]
        output.append(sum(op_numbers) + op_numbers.count(0) * query[2])
    return output


if __name__ == '__main__':
    numbers = [-5, 0]
    queries = [[2, 2, 20], [1, 2, 10]]

    print(findSum(numbers, queries))