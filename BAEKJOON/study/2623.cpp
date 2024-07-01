#include <iostream>
#include <climits>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

int N, M, num, cur, nxt, degree[1001], parent[1001];
vector<vector<int>> v;
queue<int> q, ans;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	v.resize(N + 1);
	for (int i = 1; i <= N; i++) {
		parent[i] = i;
	}
	for (int i = 0; i < M; i++) {
		cin >> num >> cur;
		for (int j = 0; j < num - 1; j++) {
			cin >> nxt;
			v[cur].push_back(nxt);
			degree[nxt]++;
			cur = nxt;
		}
	}

	int flg = 1;
	for (int i = 1; i <= N; i++) {
		if (degree[i] == 0) {
			q.push(i);
			ans.push(i);
			flg = 0;
		}
	}

	if (flg) {
		cout << 0;
		return 0;
	}

	while (!q.empty()) {
		int qp = q.front();
		q.pop();

		for (int i = 0; i < v[qp].size(); i++) {
			degree[v[qp][i]]--;
			if (degree[v[qp][i]] == 0) {
				q.push(v[qp][i]);
				ans.push(v[qp][i]);
			}
		}
	}

	for (int i = 1; i <= N; i++) {
		if (degree[i]) {
			cout << 0;
			return 0;
		}
	}

	while (!ans.empty()) {
		cout << ans.front() << '\n';
		ans.pop();
	}
}