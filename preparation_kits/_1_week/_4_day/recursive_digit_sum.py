def superDigit(n, k):
    digits = map(int, list(n))
    candidate = str(sum(digits) * k)
    if len(candidate) == 1:
        return int(candidate)
    return superDigit(candidate, 1)


if __name__ == '__main__':
    n = '9'
    k = 3
    print(superDigit(n, k))
