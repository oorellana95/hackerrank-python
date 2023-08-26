def towerBreakers(n, m):
    # If height of the towers are one, player 1 cannot move and loses
    # If the number of towers is an even number, player 2 always wins
    if m == 1 or n % 2 == 0:
        return 2
    # If the number of towers is 1 (and not of height 1) player 1 will always win
    # If the number of towers is an od number, player 1 will always wins
    return 1


if __name__ == '__main__':
    n = 2
    m = 6
    towerBreakers(n, m)
