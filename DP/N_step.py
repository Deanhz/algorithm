
F = [0, 1, 2]


def N_step(n):
    if n < 0:
        return -1
    for i in range(3, 90):
        x = F[i - 1] + F[i - 2]
        F.insert(i, x)
    return F[n]


if __name__ == '__main__':
    n = int(input('please input n:'))
    while(n < 90):
        print(N_step(n))
        n = int(input('please input n:'))
