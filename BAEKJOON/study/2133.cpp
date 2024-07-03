#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <climits>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int N, tile[31];

int dp(int n) {
	if (n == 0) return 1;
	if (n == 1) return 0;
	if (n == 2) return 3;
	if (tile[n]) return tile[n];

	int temp = 3 * dp(n - 2);
	for (int i = 4; i <= n; i+=2) {
		temp += 2 * dp(n - i);
	}
	return tile[n] = temp;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N;
	cout << dp(N);

	return 0;
}