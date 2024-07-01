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
	int y, x;
};
int N, M, year, arr[301][301], sea[301][301], visited[301][301];
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };
queue<Node> q;

int isDivided() {
	memset(visited, 0, sizeof(visited));
	int divided = -1;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (visited[i][j] || arr[i][j] == 0) continue;
			divided++;
			visited[i][j] = 1;
			q.push({ i, j });

			while (!q.empty()) {
				Node qp = q.front();
				q.pop();

				for (int d = 0; d < 4; d++) {
					int dr = qp.y + dy[d];
					int dc = qp.x + dx[d];

					if (dr < 0 || dr >= N || dc < 0 || dc >= M) continue;
					if (visited[dr][dc] || arr[dr][dc] == 0) continue;

					visited[dr][dc] = 1;
					q.push({ dr, dc });
				}
			}
		}
	}

	return divided;
}

void melt() {
	memset(sea, 0, sizeof(sea));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (arr[i][j]) continue;
			for (int d = 0; d < 4; d++) {
				int dr = i + dy[d];
				int dc = j + dx[d];

				if (dr < 0 || dr >= N || dc < 0 || dc >= M) continue;
				if (arr[dr][dc] == 0) continue;

				sea[dr][dc]++;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (arr[i][j] < sea[i][j]) arr[i][j] = 0;
			else arr[i][j] -= sea[i][j];
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}

	while (1) {
		melt();
		year++;
		int ret = isDivided();
		if (ret == -1) {
			year = 0;
			break;
		}
		else if (ret > 0) {
			break;
		}
		
	}

	cout << year << '\n';
}