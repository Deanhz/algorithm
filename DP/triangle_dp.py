import numpy as np
import pprint as pp


def MaxSum(i, j):
    if maxsum[i][j] != -1:
        return maxsum[i][j]
    if i == n - 1:
        maxsum[i][j] = D[i][j]
    else:
        x = MaxSum(i + 1, j)
        y = MaxSum(i + 1, j + 1)
        maxsum[i][j] = max(x, y) + D[i][j]
    return maxsum[i][j]


def main():
    global n, D, maxsum
    n = int(input("please input n:"))
    D = np.zeros((n, n))
    maxsum = np.zeros((n, n)) - 1
    for i in range(n):
        for j in range(i + 1):
            D[i][j] = int(input('{} line {} column:'.format(str(i), str(j))))
    pp.pprint(D)
    pp.pprint(maxsum)
    print(MaxSum(0, 0))


if __name__ == "__main__":
    main()
