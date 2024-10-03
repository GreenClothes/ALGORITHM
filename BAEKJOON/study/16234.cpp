#include<iostream>
#include<cstring>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

struct Node {
	int y, x;
};
int N, L, R, A[50][50], visited[50][50], ans;
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };
queue<Node> q;

void set_people(int y, int x, int vs, int people) {
	q.push({ y, x });
	visited[y][x] = 1e9;
	A[y][x] = people;

	while (!q.empty()) {
		Node qp = q.front();
		q.pop();

		for (int d = 0; d < 4; d++) {
			int dr = qp.y + dy[d];
			int dc = qp.x + dx[d];

			if (dr < 0 || dr >= N || dc < 0 || dc >= N) continue;
			if (visited[dr][dc] != vs) continue;
			
			visited[dr][dc] = 1e9;
			A[dr][dc] = people;
			q.push({ dr, dc });
		}
	}

	return;
}

bool move_people() {
	memset(visited, 0, sizeof(visited));

	int vs = 1, is_moved = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j]) continue;

			q.push({ i, j });
			visited[i][j] = vs;
			int num = A[i][j], cnt = 1;
			while (!q.empty()) {
				Node qp = q.front();
				q.pop();

				for (int d = 0; d < 4; d++) {
					int dr = qp.y + dy[d];
					int dc = qp.x + dx[d];

					if (dr < 0 || dr >= N || dc < 0 || dc >= N) continue;
					if (visited[dr][dc]) continue;
					if (abs(A[qp.y][qp.x] - A[dr][dc]) >= L && abs(A[qp.y][qp.x] - A[dr][dc]) <= R) {
						visited[dr][dc] = vs;
						num += A[dr][dc];
						cnt++;
						q.push({ dr, dc });
					}
				}
			}

			if (cnt > 1) {
				is_moved = 1;
				set_people(i, j, vs, num / cnt);
			}
			vs++;
		}
	}

	return is_moved;
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> L >> R;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> A[i][j];
		}
	}

	while (move_people()) ans++;

	cout << ans;
	

	return 0;
}