#!/bin/python3
import string


def missing_characters(s):
    set_to_compare = set(string.digits + string.ascii_lowercase)
    set_output = set_to_compare - set(s)
    output = list(set_output)
    output.sort()
    return "".join(output)


if __name__ == '__main__':
    print(missing_characters('123332sddsaaaaaerb'))


