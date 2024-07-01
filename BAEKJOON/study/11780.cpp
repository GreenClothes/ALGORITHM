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

#define INF 1e9
int N, M, a, b, c, cost[101][101], path[101][101];
vector<int> v;

void find_path(int start, int end) {
	if (path[start][end] == 0) {
		v.push_back(start);
		v.push_back(end);
		return;
	}
	find_path(start, path[start][end]);
	v.pop_back();
	find_path(path[start][end], end);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cost[i][j] = INF;
		}
	}
	for (int i = 0; i < M; i++) {
		cin >> a >> b >> c;
		if (cost[a][b] > c) {
			cost[a][b] = c;
		}
	}

	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j) continue;
				int next = cost[i][k] + cost[k][j];
				if (cost[i][j] > next) {
					cost[i][j] = next;
					path[i][j] = k;
				}
			}
		}
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (cost[i][j] == INF) cout << 0 << ' ';
			else cout << cost[i][j] << ' ';
		}
		cout << '\n';
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (cost[i][j] == INF) cout << 0 << ' ';
			else {
				v.clear();
				find_path(i, j);
				cout << v.size() << ' ';
				for (int s = 0; s < v.size(); s++) {
					cout << v[s] << ' ';
				}
			}
			cout << '\n';
		}
		
	}
}