#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <climits>
#include <unordered_map>
using namespace std;

int N, work[21][21], dp[21][1 << 21];

int solve(int now, int state) {
	if (state == (1 << N) - 1) return 0;
	if (dp[now][state] != -1) return dp[now][state];

	dp[now][state] = 500000;
	
	for (int i = 0; i < N; i++) {
		if (state & (1 << i)) continue;
		dp[now][state] = min(solve(now + 1, state | (1 << i)) + work[now][i], dp[now][state]);
	}

	return dp[now][state];
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> work[i][j];
		}
	}
	memset(dp, -1, sizeof(dp));

	cout << solve(0, 0);
}