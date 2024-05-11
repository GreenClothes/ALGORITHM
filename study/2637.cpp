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

struct Node {
	int make, num;
};
int N, M, X, Y, K, degree[101], num[101][101], simple[101], ans[101];
vector<vector<Node>> v, how;
queue<int> q;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	v.resize(N + 1);
	how.resize(N + 1);
	for (int i = 0; i < M; i++) {
		cin >> X >> Y >> K;
		degree[X]++;
		simple[X] = 1;
		v[Y].push_back({ X, K });
	}

	for (int i = 1; i <= N; i++) {
		if (degree[i] == 0) {
			q.push(i);
		}
	}

	while (!q.empty()) {
		int qp = q.front();
		q.pop();

		for (int i = 0; i < v[qp].size(); i++) {
			degree[v[qp][i].make]--;
			if (simple[qp]) {
				for (int j = 1; j <= N; j++) {
					if (simple[j] == 0) {
						num[v[qp][i].make][j] += num[qp][j] * v[qp][i].num;
						if(v[qp][i].make == N) ans[j] += num[qp][j] * v[qp][i].num;
					}
				}
			}
			else {
				num[v[qp][i].make][qp] += v[qp][i].num;
				if (v[qp][i].make == N) ans[qp] += v[qp][i].num;
			}
			if (degree[v[qp][i].make] == 0) {
				q.push(v[qp][i].make);
			}
		}
	}
	
	for (int i = 1; i <= N; i++) {
		if (simple[i] == 0) {
			cout << i << ' ' << ans[i] << '\n';
		}
	}
}