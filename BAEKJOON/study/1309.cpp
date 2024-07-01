#include <iostream>
using namespace std;
# define endl "\n"

int dp[100001][3];

int main() {
    int N, mod = 9901;
    cin >> N;
    dp[1][0] = 1;
    dp[1][1] = 1;
    dp[1][2] = 1;

    for (int n = 2; n <= N; n++) {
        dp[n][0] = (dp[n - 1][1] + dp[n - 1][2]) % mod;
        dp[n][1] = (dp[n - 1][0] + dp[n - 1][2]) % mod;
        dp[n][2] = (dp[n - 1][0] + dp[n - 1][1] + dp[n - 1][2]) % mod;
    }

    cout << (dp[N][0] + dp[N][1] + dp[N][2]) % mod << endl;
}