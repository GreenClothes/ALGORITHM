#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <climits>
#include <vector>
#include <queue>

using namespace std;

int N, M, A, B, degree[32001];
vector<vector<int>> v;
queue<int> q, ans;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N >> M;
	v.resize(N + 1);

	for (int i = 0; i < M; i++) {
		cin >> A >> B;
		v[A].push_back(B);
		degree[B]++;
	}

	for (int i = 1; i <= N; i++) {
		if (degree[i]) continue;
		q.push(i);
		ans.push(i);
	}

	while (!q.empty()) {
		int qp = q.front();
		q.pop();

		for (int s = 0; s < v[qp].size(); s++) {
			degree[v[qp][s]]--;
			if (degree[v[qp][s]] == 0) {
				q.push(v[qp][s]);
				ans.push(v[qp][s]);
			}
		}
	}

	while (!ans.empty()) {
		cout << ans.front() << ' ';
		ans.pop();
	}

	return 0;
}