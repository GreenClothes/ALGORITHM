#include <iostream>
#include <queue>
#include <map>
#include <climits>
#include <cstring>
#include <algorithm>
using namespace std;

int n, m, r, t[101], a, b, l, dist[101][101], max_item;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n >> m >> r;
	fill(&dist[0][0], &dist[n][n + 1], 219876543);
	for (int i = 1; i <= n; i++) {
		dist[i][i] = 0;
		cin >> t[i];
	}
	for (int i = 0; i < r; i++) {
		cin >> a >> b >> l;
		dist[a][b] = l;
		dist[b][a] = l;
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			for (int k = 1; k <= n; k++) {
				if (dist[j][k] > dist[j][i] + dist[i][k]) {
					dist[j][k] = dist[j][i] + dist[i][k];
				}
			}
		}
	}
	for (int i = 1; i <= n; i++) {
		int cnt = 0;
		for (int j = 1; j <= n; j++) {
			if (dist[i][j] <= m) cnt += t[j];
		}
		if (cnt > max_item) max_item = cnt;
	}
	cout << endl;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cout << dist[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;

	cout << max_item;
}
