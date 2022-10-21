#!/bin/python3

# Correctness test cases
# Passed 5 out of 6
# Performance test cases
# Passed 3 out of 5


def solution(S: str):
    major_distance = 0
    for i in range(len(S)-1):
        digram = S[i] + S[i+1]
        last_occurrence = S.rindex(digram)
        distance = last_occurrence - i
        if major_distance < distance:
            major_distance = distance
    return -1 if major_distance == 0 else major_distance


def solution2(S: str):
    major_distance = -1
    for i in range(len(S)-1):
        digram = S[i] + S[i+1]
        last_occurrence = S.rindex(digram)
        if last_occurrence != i:
            distance = last_occurrence - i
            if major_distance < distance:
                major_distance = distance

    return major_distance


if __name__ == '__main__':
    print(solution2("codifycosdfsfdsfsdfsdfdssdfdssd"))