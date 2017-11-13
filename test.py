import numpy as np


def func():
    buf = [0, ] * 600
    for i in range(1, 151):
        number = np.random.randint(1, 601)
        buf.insert(number, i)
    return buf


if __name__ == '__main__':
    buf = func()
    print(buf)
