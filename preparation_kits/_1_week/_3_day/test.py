import time


def palindromeIndex(s):
    # Write your code here
    reverse_s = s[::-1]
    size = len(s)

    if s == reverse_s:
        return -1

    for i in range(size // 2):
        if s[i] != reverse_s[i]:
            # Front letter
            new_str = s[:i] + s[i + 1:]
            if new_str == new_str[::-1]:
                return i

            # Back letter
            new_str = s[:size - i - 1] + s[size - i:]
            if new_str == new_str[::-1]:
                return size - i - 1

    return -1


if __name__ == '__main__':
    start = time.time()
    s = 'abaabab'
    print(palindromeIndex(s))
    end = time.time()
    print(end - start)
