#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int N, T, K[101], S[101], dp[101][10001];

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N >> T;
	for (int i = 1; i <= N; i++) {
		cin >> K[i] >> S[i];
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 0; j <= T; j++) {
			if (dp[i - 1][j - K[i]] && j >= K[i]) dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - K[i]] + S[i]);
			else if (j >= K[i]) dp[i][j] = max(dp[i - 1][j], S[i]);
			else dp[i][j] = dp[i - 1][j];
		}
	}
	
	cout << dp[N][T];

	return 0;
}