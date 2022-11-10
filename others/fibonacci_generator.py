#!/bin/python3

# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        # Same as:
        # temp_a = a
        # a = b
        # b = temp_a + b


if __name__ == '__main__':
    for x in fibon(1000000):
        print(f'{x}\n')
