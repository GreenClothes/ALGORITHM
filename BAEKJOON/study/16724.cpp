#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <climits>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int N, M, visited[1000][1000], ans, seq = 1;
char arr[1000][1000];
unordered_map<char, pair<int, int>> um = {
	{'D', {0, 1}}, {'U', {0, -1}}, {'L', {-1, 0}}, {'R', {1, 0}}
};

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (visited[i][j]) continue;
			int ny = i, nx = j;

			while (!visited[ny][nx]) {
				visited[ny][nx] = seq;
				ny += um[arr[ny][nx]].second;
				nx += um[arr[ny][nx]].first;
			}

			if (visited[ny][nx] == seq) {
				ans++;
			}
			seq++;
		}
	}

	cout << ans;

	return 0;
}