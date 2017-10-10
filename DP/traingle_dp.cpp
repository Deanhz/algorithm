//http://blog.csdn.net/baidu_28312631/article/details/47418773
//记忆递归型的动态规划
#include <iostream>
#include <algorithm>
#define MAX 101
using namespace std;

int D[MAX][MAX];
int n;
int maxsum[MAX][MAX];

int MaxSum(int i ,int j){
    if (maxsum[i][j] != -1){
        return maxsum[i][j];
    }
    if (i == n){
        maxsum[i][j] = D[i][j];
    }
    else{
        int x = MaxSum(i+1, j);
        int y = MaxSum(i+1, j+1);
        maxsum[i][j] = max(x,y) + D[i][j];
    }
    return maxsum[i][j];
}

int main(){
    int i, j;
    cout << "please input n:" << endl;
    cin >> n;
    cout << "please input triangle" << endl;
    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            cin >> D[i][j];
            maxsum[i][j] = -1;
        }
    }
    cout << MaxSum(1, 1) << endl;
    return 0;
}
