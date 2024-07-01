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
	int now, cost;

	bool operator<(Node right) const {
		if (cost > right.cost) return true;
		return false;
	}
};
int TC, n, m, t, s, g, h, a, b, d, ans[100], distS[2001], distG[2001], distH[2001];
priority_queue<Node> pq;
vector<Node> v[2001];

void dijkstra(int *visited, int start) {
	
	visited[start] = 0;
	pq.push({ start, 0 });

	while (!pq.empty()) {
		Node qp = pq.top();
		pq.pop();
		
		for (int i = 0; i < v[qp.now].size(); i++) {
			Node next = v[qp.now][i];
			int temp_cost = qp.cost + next.cost;
			if (visited[next.now] <= temp_cost) continue;
			visited[next.now] = temp_cost;
			pq.push({ next.now, temp_cost });
		}
	}
}

void init() {
	for (int i = 1; i <= n; i++) {
		distS[i] = INT_MAX;
		distG[i] = INT_MAX;
		distH[i] = INT_MAX;
		v[i].clear();
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> TC;
	while (TC--) {
		cin >> n >> m >> t;
		cin >> s >> g >> h;
		init();
		
		for (int i = 0; i < m; i++) {
			cin >> a >> b >> d;

			v[a].push_back({ b, d });
			v[b].push_back({ a, d });
		}

		dijkstra(distS, s);
		dijkstra(distG, g);
		dijkstra(distH, h);
		for (int i = 0; i < t; i++) {
			cin >> ans[i];
		}
		sort(ans, ans + t);

		for (int i = 0; i < t; i++) {
			if (distS[ans[i]] == INT_MAX || distH[ans[i]] == INT_MAX || distG[ans[i]] == INT_MAX) continue;
			if (distS[ans[i]] >= distS[g] + distG[h] + distH[ans[i]] || distS[ans[i]] >= distS[h] + distG[ans[i]] + distH[g]) cout << ans[i] << ' ';
		}
		cout << '\n';
	}
}