#!/bin/python3
import string


#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weighted_uniform_strings_not_optimal(s, queries):
    base_weights = dict((j, i+1) for i, j in enumerate("abcdefghijklmnopqrstuvwxyz"))
    weights = []

    for i in range(len(s)):
        weight = base_weights.get(s[i])
        if i != 0 and s[i-1] == s[i]:
            weights.append(weights[i-1] + weight)
        else:
            weights.append(weight)

    answer = []
    for q in queries:
        answer.append('Yes' if q in weights else 'No')
    return answer


def weighted_uniform_strings_optimal(s, queries):
    alphabet = string.ascii_lowercase
    weights = set()
    value = 0
    last_char = ''
    for char in s:
        weight = alphabet.index(char) + 1
        if last_char == char:
            value += weight
            weights.add(value)
        else:
            weights.add(weight)
            value = weight
            last_char = char

    output = ['Yes' if query in weights else 'No' for query in queries]
    return output


def weighted_uniform_strings(s, queries):
    alphabet = string.ascii_lowercase

    # get weight for contiguous substrings
    sub = set()
    last = ''
    value = 0
    for char in s:
        weight = alphabet.index(char) + 1
        if char == last:
            value += weight
            sub.add(value)
        else:
            sub.add(weight)
            last = char
            value = weight

    # check if queries exist in substring
    output = ['Yes' if query in sub else 'No' for query in queries]

    return output

if __name__ == '__main__':
    s = 'abbcccdddd'
    queries = [1, 7, 5, 4, 15]
    print(weighted_uniform_strings_optimal(s, queries))
