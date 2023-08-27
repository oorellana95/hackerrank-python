def minimumBribes(q):
    q = [i - 1 for i in q]
    bribes = 0
    for desired_position, original_position in enumerate(q):
        bribe = original_position - desired_position
        if bribe > 2:
            print('Too chaotic')
            return
        for current_position in q[max(original_position-1, 0):desired_position]:
            if current_position > original_position:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    q = [2, 1, 5, 3, 4]
    minimumBribes(q)
