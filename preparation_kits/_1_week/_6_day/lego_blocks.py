def legoBlocks(n, m):
    MOD = (10 ** 9 + 7)

    # Step 1: O(W)
    # The number of combinations to build a single row
    # As only four kinds of sizes, so
    # base case:
    # if width is 0, combination is 1
    # if width is 1, combination is 1
    # if width is 2, combination is 2
    # if width is 3, combination is 4
    row_combinations = [1, 1, 2, 4]

    # Build row combinations up to current wall's width
    while len(row_combinations) <= m:
        row_combinations.append(sum(row_combinations[-4:]) % MOD)

    # Step 2: O(W)
    # Compute total combinations
    # for constructing a wall of height N of varying widths
    total = [pow(c, n, MOD) for c in row_combinations]

    # Step 3: O(W^2)
    # Find the number of unstable wall configurations
    # for a wall of height N of varying widths
    unstable = [0, 0]

    # Divide the wall into left part and right part,
    # and calculate the combination of left part and right part.
    # From width is 2, we start to consider about violation.
    for i in range(2, m + 1):
        # i: current total width
        # j: left width
        # i - j: right width
        # f: (left part - previous vertical violation)*right part
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)

    # Print the number of stable wall combinations
    return (total[m] - unstable[m]) % MOD

if __name__ == '__main__':
    height = 2
    width = 3
    legoBlocks(n=height, m=width)
