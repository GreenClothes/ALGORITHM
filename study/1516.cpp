#include <iostream>
#include <climits>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

int N, input, degree[501], t[501], ans[501];
vector<vector<int>> v;
queue<int> q;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	v.resize(N + 1);
	for (int i = 1; i <= N; i++) {
		cin >> t[i];
		while (true) {
			cin >> input;
			if (input == -1) break;
			v[input].push_back(i);
			degree[i]++;
		}
	}

	for (int i = 1; i <= N; i++) {
		if (degree[i] == 0) {
			ans[i] = t[i];
			q.push(i);
		}
	}

	while (!q.empty()) {
		int qp = q.front();
		q.pop();

		for (int i = 0; i < v[qp].size(); i++) {
			degree[v[qp][i]]--;
			ans[v[qp][i]] = max(ans[v[qp][i]], ans[qp]);
			if (degree[v[qp][i]] == 0) {
				ans[v[qp][i]] += t[v[qp][i]];
				q.push(v[qp][i]);
			}
		}
	}

	for (int i = 1; i <= N; i++) {
		cout << ans[i] << '\n';
	}
}