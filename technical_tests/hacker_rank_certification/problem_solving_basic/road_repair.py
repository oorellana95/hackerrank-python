#!/bin/python3
from typing import List


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#


def getMinCost(crew_id: List[int], job_id: List[int]):
    cost = 0
    crew_id.sort()
    job_id.sort()
    if len(crew_id) == len(job_id):
        for i in range(len(crew_id)):
            if job_id[i] >= crew_id[i]:
                cost += job_id[i] - crew_id[i]
            else:
                cost += crew_id[i] - job_id[i]
    return cost


if __name__ == '__main__':
    crew_id = [2, 2, 20]
    job_id = [2, 2, 20]

    print(getMinCost(crew_id, job_id))