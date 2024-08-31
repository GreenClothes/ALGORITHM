#include<iostream>


using namespace std;

int n, m, x, y, sx, sy, visited[5][5], map[5][5], seq[5][5], ans;
int dy[] = { -1, 1, 0, 0 }, dx[] = { 0, 0, -1, 1 };

void dfs(int ny, int nx, int nseq) {

	if (seq[ny][nx] == nseq + 1) nseq++;
	else if (seq[ny][nx] > nseq + 1) return;

	if (nseq == m) {
		ans++;
		nseq--;
		return;
	}

	for (int d = 0; d < 4; d++) {
		int dr = ny + dy[d];
		int dc = nx + dx[d];

		if (dr <= 0 || dr > n || dc <= 0 || dc > n) continue;
		if (visited[dr][dc] || map[dr][dc] == 1) continue;

		visited[dr][dc] = 1;
		dfs(dr, dc, nseq);
		visited[dr][dc] = 0;
	}

	if (seq[ny][nx] == nseq) nseq--;
}

int main(int argc, char** argv)
{
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> map[i][j];
		}
	}

	cin >> sy >> sx;
	seq[sy][sx] = 1;
	for (int i = 2; i <= m; i++) {
		cin >> y >> x;
		seq[y][x] = i;
	}

	visited[sy][sx] = 1;
	dfs(sy, sx, 1);

	cout << ans;

	return 0;
}