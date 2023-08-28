def cmap(funcs, arr):
    for i in arr:
        x = i
        for f in funcs:
            x = f(x)
        yield x


if __name__ == '__main__':
    funcs = [lambda x: x * x, lambda x: x + 3]
    arr = [1, 2, 3, 4]
    result = cmap(funcs, arr)
    output = []
    for result_item in result:
        output.append(result_item)

    print(output)