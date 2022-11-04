#!/bin/python3

def tuple_list(arr):
    return [(int(a), int(a)**2) for a in arr]


if __name__ == '__main__':
    name = input()
    exercise_list = name.replace('[', ''). replace(']', ''). split(',')
    print(tuple_list(exercise_list))


