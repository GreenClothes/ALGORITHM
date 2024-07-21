#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>

using namespace std;

int N, M, arr[1000][1000], dp[1000][1000][3], visited[1000][1000];
int dy[] = { 1, 0, 0 }, dx[] = { 0, -1, 1 };

int dfs(int y, int x, int direc) {
	if (y == N - 1 && x == M - 1) return arr[y][x];
	if (dp[y][x][direc] != -1e9) return dp[y][x][direc];

	visited[y][x] = 1;
	int temp = -1e9;
	for (int d = 0; d < 3; d++) {
		int dr = y + dy[d];
		int dc = x + dx[d];

		if (dr < 0 || dr >= N || dc < 0 || dc >= M) continue;
		if (visited[dr][dc]) continue;

		temp = max(temp, dfs(dr, dc, d));
	}
	visited[y][x] = 0;
	dp[y][x][direc] = arr[y][x] + temp;
	return dp[y][x][direc];
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
			for (int d = 0; d < 3; d++) dp[i][j][d] = -1e9;
		}
	}
	
	cout << dfs(0, 0, 0);

	return 0;
}