#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 101

int D[MAX][MAX];
int * maxsum;
int n;

int main(){
    int i,j;
    cout << "please input n:"<< endl;
    cin >> n;
    cout << "please input triangle data:" << endl;
    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            cin >> D[i][j];
        }
    }
    maxsum = D[n];
    for(i=n-1;i>=1;i--){
        for(j=1;j<=i;i++){
            maxsum[j] = max(maxsum[j],maxsum[j+1]) + D[i][j];
        }
    }
    cout << maxsum[1] << endl;
}