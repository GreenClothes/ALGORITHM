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
int N, M, arr[1001][1001], visited[1001][1001], ny, nx, ey, ex;
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };
char input;
queue<Node> ghost, q;

void move_ghost() {
	int g_size = ghost.size();
	for (int gs = 0; gs < g_size; gs++) {
		Node qp = ghost.front();
		ghost.pop();

		for (int d = 0; d < 4; d++) {
			int dr = qp.y + dy[d];
			int dc = qp.x + dx[d];

			if (dr < 0 || dr >= N || dc < 0 || dc >= M) continue;
			if (arr[dr][dc] == 2) continue;

			arr[dr][dc] = 2;
			ghost.push({ dr, dc });
		}
	}
}

bool escape() {
	q.push({ ny, nx });
	visited[ny][nx] = 1;

	while (!q.empty()) {
		move_ghost();

		int q_size = q.size();
		for (int qs = 0; qs < q_size; qs++) {
			Node qp = q.front();
			q.pop();

			if (qp.y == ey && qp.x == ex) return true;

			for (int d = 0; d < 4; d++) {
				int dr = qp.y + dy[d];
				int dc = qp.x + dx[d];

				if (dr < 0 || dr >= N || dc < 0 || dc >= M) continue;
				if (visited[dr][dc]) continue;
				if (arr[dr][dc]) continue;

				visited[dr][dc] = 1;
				q.push({ dr, dc });
			}
		}
	}

	return false;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> input;
			if (input == '#') {
				arr[i][j] = 1;
			}
			else if (input == 'N') {
				ny = i;
				nx = j;
			}
			else if (input == 'D') {
				ey = i;
				ex = j;
			}
			else if (input == 'G') {
				ghost.push({ i, j });
				arr[i][j] = 2;
			}
		}
	}

	if (escape()) cout << "Yes";
	else cout << "No";
}
