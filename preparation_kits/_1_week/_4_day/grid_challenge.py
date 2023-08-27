def gridChallenge(grid):
    # Sort rows by
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    # Check columns
    columns = [list(column) for column in zip(*grid)]
    for column in columns:
        if column != sorted(column):
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    grid = ['zxyrl', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    print(gridChallenge(grid))
