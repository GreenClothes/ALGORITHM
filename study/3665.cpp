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

int TC, n, ti[501], graph[501][501], degree[501], ans[501], m, ai, bi;
queue<int> q;

void init() {
	memset(ti, 0, sizeof(ti));
	memset(graph, 0, sizeof(graph));
	memset(degree, 0, sizeof(degree));
	memset(ans, 0, sizeof(ans));
	while (!q.empty()) q.pop();
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> TC;
	for (int tc = 0; tc < TC; tc++) {
		init();

		cin >> n;
		for (int i = 1; i <= n; i++) {
			cin >> ti[i];
			for (int j = 1; j < i; j++) {
				graph[ti[j]][ti[i]] = 1;
				degree[ti[i]]++;
			}
		}

		cin >> m;
		for (int i = 0; i < m; i++) {
			cin >> ai >> bi;
			if (graph[ai][bi]) {
				graph[ai][bi] = 0;
				graph[bi][ai] = 1;
				degree[ai]++;
				degree[bi]--;
			}
			else if (graph[bi][ai]) {
				graph[bi][ai] = 0;
				graph[ai][bi] = 1;
				degree[ai]--;
				degree[bi]++;
			}
		}

		for (int i = 1; i <= n; i++) {
			if (degree[i] == 0) {
				q.push(i);
			}
		}

		int flg = 1;
		for (int i = 1; i <= n; i++) {
			if (q.empty()) {
				cout << "IMPOSSIBLE\n";
				flg = 0;
				break;
			}
			if (q.size() > 1) {
				cout << "?\n";
				flg = 0;
				break;
			}

			int qp = q.front();
			ans[i] = qp;
			degree[qp]--;
			q.pop();
			for (int j = 1; j <= n; j++) {
				if (graph[qp][j]) degree[j]--;
				if (degree[j] == 0) q.push(j);
			}
		}

		if (flg) {
			for (int i = 1; i <= n; i++) {
				cout << ans[i] << ' ';
			}
			cout << '\n';
		}
	}
}