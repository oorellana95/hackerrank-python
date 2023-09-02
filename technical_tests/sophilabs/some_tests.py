#!/bin/python3

def test(i,j):
  if i == 0:
    return j
  else:
    return test(i-1,i+j)


def test_1():
    n = 3
    a = "Sophilabs";
    print(a * n)


def test_2():
    college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    print(list(enumerate(college_years, 2019)))


def test_3():
    a = [3, 4, 5, 20, 5, 25, 1, 3]
    a.pop()
    print(a)

def test_4():
    print(all([2,4,0,6]))


def test_5():
    if bool(1):
        print("Foo")
    elif bool(89):
        print("Bar")
    elif float("Baz"):
        print("Baz")
    else:
        print("Que")

def test_6():
    print(print(9//2))


if __name__ == '__main__':
    print(test(1,8))











