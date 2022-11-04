#!/bin/python3

class HackerEarth:
    def __init__(self, h = 1):
        self.h = h

    def set(self, h):
        self.h = h
        return h


def tuple_list(arr):
    return [(int(a), int(a)**2) for a in arr]


if __name__ == '__main__':
    hack = HackerEarth()
    print(hack.set(hack.h + 1))


