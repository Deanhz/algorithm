//http://blog.csdn.net/baidu_28312631/article/details/47418773
//递归
#include <iostream>
#include <algorithm>
#define MAX 101
using namespace std;

int D[MAX][MAX];
int n;

int MaxSum(int i, int j){
    if (i==n)
        return D[i][j];
    int x = MaxSum(i+1, j);
    int y = MaxSum(i+1, j+1);
    return max(x,y) + D[i][j];
}

int main(){
    int i, j;
    cout <<"please input n:"<< endl;
    cin >> n;
    cout << "please input triangle" << endl;
    for (i=1;i<=n;i++)
        for(j=1;j<=i;j++)
            cin >> D[i][j];
    cout <<MaxSum(1,1) <<endl;
    return 0;
}
