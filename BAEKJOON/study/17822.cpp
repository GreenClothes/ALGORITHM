#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <string>
#include <cstring>

using namespace std;

struct Node {
	int y, x;
};
int N, M, T, x, d, k, arr[51][51], ans;
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };
queue<Node> q;

void rotate() {
	int board = x - 1;
	while (board < N) {
		if (d == 0) {
			for (int j = 0; j < k; j++) {
				int before = arr[board][0];

				for (int i = 1; i <= M; i++) {
					int next = arr[board][i % M];
					arr[board][i % M] = before;
					before = next;
				}
			}
		}
		else if (d == 1) {
			for (int j = 0; j < k; j++) {
				int before = arr[board][0];

				for (int i = M - 1; i >= 0; i--) {
					int next = arr[board][i];
					arr[board][i] = before;
					before = next;
				}
			}
		}

		board += x;
	}
}

void del_num() {
	int isdel = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (arr[i][j] == 0) continue;

			int nownum = arr[i][j];
			for (int d = 0; d < 4; d++) {
				int dr = i + dy[d];
				int dc = j + dx[d];

				if (dc >= M) dc %= M;
				else if (dc < 0) dc = M - dc;

				if (dr < 0 || dr >= N) continue;
				if (arr[dr][dc] != nownum) continue;

				isdel = 1;
				arr[dr][dc] = 0;
				q.push({ dr, dc });
			}
			if (q.empty()) continue;


			arr[i][j] = 0;
			while (!q.empty()) {
				Node qp = q.front();
				q.pop();

				for (int d = 0; d < 4; d++) {
					int dr = qp.y + dy[d];
					int dc = qp.x + dx[d];

					if (dc >= M) dc %= M;
					else if (dc < 0) dc = M + dc;

					if (dr < 0 || dr >= N) continue;
					if (arr[dr][dc] != nownum) continue;

					arr[dr][dc] = 0;
					q.push({ dr, dc });
				}
			}
		}
	}

	if (isdel == 0) {
		int sum = 0, cnt = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 0) continue;
				sum += arr[i][j];
				cnt++;
			}
		}

		double mean = (double)sum / (double)cnt;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 0) continue;
				
				if (arr[i][j] > mean) arr[i][j]--;
				else if (arr[i][j] < mean) arr[i][j]++;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M >> T;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}

	for (int t = 0; t < T; t++) {
		cin >> x >> d >> k;
		rotate();

		cout << endl;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cout << arr[i][j] << " ";
			}
			cout << endl;
		}
		cout << endl;

		del_num();

		cout << endl;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cout << arr[i][j] << " ";
			}
			cout << endl;
		}
		cout << endl;
	}

	

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (arr[i][j] == 0) continue;
			ans += arr[i][j];
		}
	}
	
	cout << ans;
}