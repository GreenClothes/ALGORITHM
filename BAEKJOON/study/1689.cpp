#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <climits>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int N, s, e, ans, now;
pair<int, int> line[2000001];

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> s >> e;
		line[i] = { s, 1 };
		line[i + N] = { e, -1 };
	}
	sort(line, line + 2 * N);
	for (int i = 0; i < 2 * N; i++) {
		now += line[i].second;
		ans = max(ans, now);
	}
	cout << ans;

	return 0;
}