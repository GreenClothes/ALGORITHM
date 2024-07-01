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
	int a, b, weight;

	bool operator<(Node right) {
		if (weight > right.weight) return true;
		else return false;
	}
};
int N, M, A, B, C, F1, F2, parent[100001];
vector<Node> v;

int find_parent(int a) {
	if (a == parent[a]) return a;
	return parent[a] = find_parent(parent[a]);
}

void union_parent(int a, int b) {
	a = find_parent(a);
	b = find_parent(b);

	if (a == b) return;

	if (a < b) parent[b] = a;
	else if (a > b) parent[a] = b;

	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		parent[i] = i;
	}
	for (int i = 0; i < M; i++) {
		cin >> A >> B >> C;
		v.push_back({ A, B, C });
	}
	sort(v.begin(), v.end());
	cin >> F1 >> F2;

	for (int i = 0; i < M; i++) {
		union_parent(v[i].a, v[i].b);
		if (find_parent(F1) == find_parent(F2)) {
			cout << v[i].weight;
			return 0;
		}
	}
}