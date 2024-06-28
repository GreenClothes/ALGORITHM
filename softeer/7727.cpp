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
	int y[3], x[3], fruit;
};
int N, M, arr[21][21], visited[21][21], y, x, ans;
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };
Node friends;
queue<Node> q;

void get_fruit(Node node, int depth, int fdepth) {
	if (fdepth == M) {
		ans = max(ans, node.fruit);
		return;
	}
	if (depth == 3) {
		get_fruit(node, 0, fdepth + 1);
		return;
	}

	Node loc = node;

	for (int d = 0; d < 4; d++) {
		int dr = loc.y[fdepth] + dy[d];
		int dc = loc.x[fdepth] + dx[d];

		if (dr <= 0 || dr > N || dc <= 0 || dc > N) continue;
		
		if (visited[dr][dc] == 0) node.fruit += arr[dr][dc];
		visited[dr][dc] |= (1 << (depth + 1 + fdepth * 4));
		node.y[fdepth] = dr; node.x[fdepth] = dc;
		get_fruit(node, depth + 1, fdepth);
		visited[dr][dc] &= ~(1 << (depth + 1 + fdepth * 4));
		node = loc;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> arr[i][j];
		}
	}
	for (int i = 0; i < M; i++) {
		cin >> y >> x;
		friends.y[i] = y;
		friends.x[i] = x;
		friends.fruit += arr[y][x];
		visited[y][x] |= (1 << i * 4);
	}

	get_fruit(friends, 0, 0);


	cout << ans;
}