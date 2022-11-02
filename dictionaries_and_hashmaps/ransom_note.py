#!/bin/python3
from typing import List
from collections import Counter

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


# Checking if all words are in the magazine (it does not take into account if some word repeats)
def check_magazine_all(magazine: List[str], note: List[str]):
    if all(word in magazine for word in note):
        return 'Yes'
    return 'No'


# Time limit exceeded
def check_magazine_time(magazine: List[str], note: List[str]):
    response = 'Yes'
    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            response = 'No'
            break
    print(response)


def check_magazine(magazine: List[str], note: List[str]):
    output = 'No'
    magazine_counter = Counter(magazine)
    note_counter = Counter(note)
    if magazine_counter & note_counter == note_counter:
        output = 'Yes'
    print(output)


if __name__ == '__main__':
    magazine = "give me one grand today night".rstrip().split()
    note = "give one grand today".rstrip().split()
    check_magazine(magazine=magazine, note=note)
