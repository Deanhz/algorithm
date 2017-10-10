//递推型动态规划(非递归)
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 101

int D[MAX][MAX];
int n;
int maxsum[MAX][MAX];

int main(){
    int i, j;
    cout << "please input n:"<< endl;
    cin >> n;
    cout << "please input triangle:"<< endl;
    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            cin >> D[i][j];
            maxsum[i][j] = -1;
        }
    }
    for(i=1;i<=n;i++){
        maxsum[n][i] = D[n][i];
    }
    for(i=n-1;i>=1;i--){
        for(j=1;j<=i;j++){
            maxsum[i][j] = max(maxsum[i+1][j],maxsum[i+1][j+1]) + D[i][j];
        }
    }
    cout << maxsum[1][1] << endl;
}
