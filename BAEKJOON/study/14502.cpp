#include<iostream>
#include<cstring>
#include<queue>
#include<algorithm>

using namespace std;

struct Node {
	int y, x;
};

queue<Node> q;

int N, M, visited[8][8], lab[8][8];
int ny1, nx1, ny2, nx2, ny3, nx3, ans;
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };

void check_safe() {
	memset(visited, 0, sizeof(visited));

	int res = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (lab[i][j] == 1) {
				res++;
			}
			else if (lab[i][j] == 2 && !visited[i][j]) {
				q.push({ i, j });
				visited[i][j] = 1;

				while (!q.empty()) {
					Node qp = q.front();
					q.pop();
					res++;

					for (int d = 0; d < 4; d++) {
						int dr = qp.y + dy[d];
						int dc = qp.x + dx[d];

						if (dr < 0 || dr >= N || dc < 0 || dc >= M) continue;
						if (visited[dr][dc] || lab[dr][dc] == 1) continue;

						visited[dr][dc] = 1;
						q.push({ dr, dc });
					}
				}
			}
		}
	}
	ans = max(ans, N * M - res);
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> lab[i][j];
		}
	}

	for (int i = 0; i < N * M - 2; i++) {
		ny1 = i / M;
		nx1 = i % M;
		if (lab[ny1][nx1]) continue;

		for (int j = i + 1; j < N * M - 1; j++) {
			ny2 = j / M;
			nx2 = j % M;
			if (lab[ny2][nx2]) continue;

			for (int k = j + 1; k < N * M; k++) {
				ny3 = k / M;
				nx3 = k % M;
				if (lab[ny3][nx3]) continue;

				lab[ny1][nx1] = 1;
				lab[ny2][nx2] = 1;
				lab[ny3][nx3] = 1;
				check_safe();
				lab[ny1][nx1] = 0;
				lab[ny2][nx2] = 0;
				lab[ny3][nx3] = 0;
			}
		}
	}

	cout << ans;

	return 0;
}