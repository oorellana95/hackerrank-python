if __name__ == '__main__':
    no_inputs = int(input())
    inputs = []
    for i in range(no_inputs):
        inputs.append(input().split(' '))

    s = ""
    history = []
    for i in inputs:
        if i[0] == '1':
            to_append = i[1]
            history.append(s)
            s += to_append
        elif i[0] == '2':
            k = int(i[1])
            history.append(s)
            s = s[:-k]
        elif i[0] == '3':
            k = int(i[1])
            print(s[k - 1])
        elif i[0] == '4':
            s = history.pop()
