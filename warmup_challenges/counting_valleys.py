#!/bin/python3

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def counting_valleys(steps: int, path: str):
    valleys = 0
    from_sea_level = 0

    for step in path:
        if step == 'U':
            from_sea_level = from_sea_level + 1
            if from_sea_level == 0:
                valleys = valleys + 1
        elif step == 'D':
            from_sea_level = from_sea_level - 1

    return valleys


if __name__ == '__main__':
    steps = 8
    path = 'UDDDUDUU'
    print(counting_valleys(steps=steps, path=path))
