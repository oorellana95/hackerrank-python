def run():
    n = 100
    s = []
    while n > 0:
        s.append(n % 2 == 0)
        n = n // 2
    while len(s) > 0:
        print(int(s.pop()))


if __name__ == '__main__':
    run()
