'''
最长递增子序列问题
2017.10.17
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学不交换位置就能排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1, 2, …, K，他们的身高分别为T1, T2, …, TK，
则他们的身高满足T1 < T2 < … < Ti , Ti > Ti+1 > … > TK (1 <= i <= K)。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
输入：
输入的第一行是一个整数N（2 <= N <= 100），表示同学的总数。
第一行有n个整数，用空格分隔，第i个整数Ti（130 <= Ti <= 230）是第i位同学的身高（厘米）。
输出：
可能包括多组测试数据，对于每组数据，
输出包括一行，这一行只包含一个整数，就是最少需要几位同学出列。
样例输入：
8
186 186 150 200 160 130 197 220
样例输出：
4
'''


def func():
    N = int(input())
    # data = list(map(int, input().split()))
    data = [186, 186, 150, 200, 160, 130, 197, 220]
    left = [0] * N
    right = [0] * N
    left[0] = right[N - 1] = 1
    for i in range(1, N):
        max_left = 1
        for j in range(0, i):
            if data[j] < data[i]:
                max_left = max(max_left, left[j] + 1)
        left[i] = max_left
    for i in range(0, N - 1)[::-1]:
        max_right = 1
        for j in range(i + 1, N - 1):
            if data[j] < data[i]:
                max_right = max(max_right, right[j] + 1)
        right[i] = max_right
    print(left)
    print(right)
    sumLF = []
    for i in range(N):
        sumLF.append(left[i] + right[i])
    return max(sumLF) - 1


if __name__ == '__main__':
    while(1):
        print(func())
