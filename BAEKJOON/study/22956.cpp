#include <iostream>
#include <climits>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

int N, M, Q, a, b, c, height[1001][1001], rain[1001][1001], parent[1001][1001][2];
int dr, dc, dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };

pair<int, int> find_parent(int y, int x) {
	if (parent[y][x][0] == 0) {
		parent[y][x][0] = y;
		parent[y][x][1] = x;
		return make_pair(y, x);
	}
	if (parent[y][x][0] == y && parent[y][x][1] == x) {
		return make_pair(y, x);
	}
	pair<int, int> p = find_parent(parent[y][x][0], parent[y][x][1]);
	parent[y][x][0] = p.first;
	parent[y][x][1] = p.second;

	return p;
}

void union_parent(int ay, int ax, int by, int bx) {
	pair<int, int> pa = find_parent(ay, ax);
	pair<int, int> pb = find_parent(by, bx);

	if (pa.first == pb.first && pa.second == pb.second) return;

	if (height[pa.first][pa.second] < height[pb.first][pb.second]) {
		parent[pb.first][pb.second][0] = pa.first;
		parent[pb.first][pb.second][1] = pa.second;
		return;
	}
	else if (height[pa.first][pa.second] > height[pb.first][pb.second]) {
		parent[pa.first][pa.second][0] = pb.first;
		parent[pa.first][pa.second][1] = pb.second;
		return;
	}

	if (rain[pa.first][pa.second] > rain[pb.first][pb.second]) {
		parent[pb.first][pb.second][0] = pa.first;
		parent[pb.first][pb.second][1] = pa.second;
	}
	else if (rain[pa.first][pa.second] < rain[pb.first][pb.second]) {
		parent[pa.first][pa.second][0] = pb.first;
		parent[pa.first][pa.second][1] = pb.second;
	}
	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M >> Q;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> height[i][j];
		}
	}

	for (int i = 1; i <= Q; i++) {
		cin >> a >> b >> c;
		height[a][b] -= c;
		rain[a][b] = -i;

		pair<int, int> p = find_parent(a, b);
		if (height[a][b] < height[p.first][p.second]) {
			parent[p.first][p.second][0] = a;
			parent[p.first][p.second][1] = b;
			parent[a][b][0] = a;
			parent[a][b][1] = b;
		}

		for (int d = 0; d < 4; d++) {
			int dr = a + dy[d];
			int dc = b + dx[d];

			if (dr <= 0 || dr > N || dc <= 0 || dc > M) continue;
			if (rain[dr][dc] >= 0) continue;
			union_parent(a, b, dr, dc);
		}
		p = find_parent(a, b);
		cout << p.first << ' ' << p.second << '\n';
	}
}