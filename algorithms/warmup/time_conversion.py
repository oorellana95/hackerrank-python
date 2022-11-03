#!/bin/python3
from datetime import datetime

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def time_conversion(s):
    datetime_object = datetime.strptime(s, '%I:%M:%S%p')
    return datetime_object.strftime("%H:%M:%S")


if __name__ == '__main__':
    print(time_conversion("07:05:45PM"))
