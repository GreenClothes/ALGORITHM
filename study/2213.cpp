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

int N, W[10001], visited[10001], a, b, dp[10001][2], ans;
vector<vector<int>> v;
vector<int> path;

void search(int now) {
	dp[now][0] = 0;
	dp[now][1] = W[now];

	visited[now] = 1;

	for (int i = 0; i < v[now].size(); i++) {
		int next = v[now][i];
		if (visited[next]) continue;
		search(next);

		dp[now][0] += max(dp[next][0], dp[next][1]);
		dp[now][1] += dp[next][0];
	}
}

void search_path(int now, int before) {
	if (dp[now][1] > dp[now][0] && !visited[before]) {
		path.push_back(now);
		visited[now] = 1;
	}

	for (int i = 0; i < v[now].size(); i++) {
		int next = v[now][i];
		if (next == before) continue;
		search_path(next, now);
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	v.resize(N + 1);
	for (int i = 1; i <= N; i++) {
		cin >> W[i];
	}

	for (int i = 0; i < N-1; i++) {
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}

	search(1);
	memset(visited, 0, sizeof(visited));
	search_path(1, 0);

	sort(path.begin(), path.end());
	cout << max(dp[1][0], dp[1][1]) << '\n';
	for (int i = 0; i < path.size(); i++) {
		cout << path[i] << ' ';
	}
}