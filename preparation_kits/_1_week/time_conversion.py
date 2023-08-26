import time
from datetime import datetime


def timeConversion(s):
    t = datetime.strptime(s, '%I:%M:%S%p')
    return t.strftime('%H:%M:%S')


if __name__ == '__main__':
    start = time.time()
    s = "07:05:45PM"
    print(timeConversion(s))
    end = time.time()
    print(end - start)
