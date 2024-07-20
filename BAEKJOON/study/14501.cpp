#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

int N, plan[16][2], dp[17], ans;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> plan[i][0] >> plan[i][1];
	}
	if (plan[1][0] <= N) dp[plan[1][0]] = plan[1][1];
	for (int i = 2; i <= N; i++) {
		if (i + plan[i][0] - 1 > N) continue;
		for (int j = 1; j < i; j++) {
			dp[i + plan[i][0] - 1] = max(dp[i + plan[i][0] - 1], dp[j] + plan[i][1]);
		}
	}
	for (int i = 1; i <= N; i++) {
		ans = max(ans, dp[i]);
	}
	cout << ans;

	return 0;
}