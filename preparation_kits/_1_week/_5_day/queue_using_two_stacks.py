
if __name__ == '__main__':
    q = int(input())
    _queue = []

    for i in range(q):
        _input = input().split(" ")
        q_type = _input[0]
        if q_type == "1":
            _queue.append(_input[1])
        elif q_type == "2":
            _queue.pop(0)
        else:
            print(_queue[0])

