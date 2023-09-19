#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#


def contacts(queries):
    contacts_list = []
    results = []
    for query in queries:
        operator = query[0]
        name = ' '.join(query[1:])
        if operator == "add":
            contacts_list.append(name)
        elif operator == "find":
            matching = len([s for s in contacts_list if name in s])
            results.append(matching)

    return results


if __name__ == '__main__':

    queries_rows = 4
    queries_input = ['add hack run', 'add hackerrank', 'find hac', 'find hak']
    queries = []
    for query in queries_input:
        queries.append(query.rstrip().split())

    result = contacts(queries)

    print(result)
