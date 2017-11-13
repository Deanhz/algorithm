'''
最长递增子序列问题
2017.10.17
某国为了防御敌国的导弹袭击,开发出一种导弹拦截系统。但是这种导弹拦
截系统有一个缺陷:虽然它的第一发炮弹能够到达任意的高度,但是以后每一发
炮弹都不能高于前一发的高度。某天,雷达捕捉到敌国的导弹来袭,并观测到导
弹依次飞来的高度,请计算这套系统最多能拦截多少导弹。拦截来袭导弹时,必
须按来袭导弹袭击的时间顺序,不允许先拦截后面的导弹,再拦截前面的导弹。
输入:
每组输入有两行,
第一行,输入雷达捕捉到的敌国导弹的数量 k(k<=25),
第二行,输入 k 个正整数,表示 k 枚导弹的高度,按来袭导弹的袭击时间顺
序给出,以空格分隔。
输出:
每组输出只有一行,包含一个整数,表示最多能拦截多少枚导弹。
样例输入:
8
300 207 155 300 299 170 158 65
样例输出:
6
'''


def func():
    k = int(input())
    data = list(map(int, input().split()))
    # data = [300, 207, 155, 300, 299, 170, 158, 65]
    F = [0] * k
    F[0] = 1
    for i in range(1, k):
        max_data = 1
        for j in range(0, i):
            if (data[j] >= data[i]):
                max_data = max(max_data, F[j] + 1)
        F[i] = max_data
    print(F)
    return F[k - 1]


if __name__ == '__main__':
    while(True):
        print(func())
