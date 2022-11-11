#!/bin/python3

def avg(*nums):
    list_nums = list(nums)
    return sum(list_nums) / len(list_nums)


if __name__ == '__main__':
    print(avg(2, 5, 10))


