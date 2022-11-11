#!/bin/python3

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthday_cake_candles(candles):
    highest_candle = max(candles)
    return candles.count(highest_candle)


if __name__ == '__main__':
    candles = [4, 4, 1, 3]
    print(birthday_cake_candles(candles))
