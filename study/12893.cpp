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
#include <set>
using namespace std;

int N, M, A, B, parent[2001], enemy[2001];

int find_parent(int a) {
	if (a == parent[a]) return a;
	return parent[a] = find_parent(parent[a]);
}

int union_parent(int a, int b) {
	a = find_parent(a);
	b = find_parent(b);

	if (a == b) return a;

	if (a < b) {
		parent[b] = a;
		return a;
	}
	else if (b < a) {
		parent[a] = b;
		return b;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		parent[i] = i;
	}
	for (int i = 0; i < M; i++) {
		cin >> A >> B;
		int pA = find_parent(A), pB = find_parent(B);
		if (pA == pB) {
			cout << 0;
			return 0;
		}
		
		if (enemy[pA] == 0) enemy[pA] = pB;
		else enemy[pA] = union_parent(pB, enemy[pA]);

		if (enemy[pB] == 0) enemy[pB] = pA;
		else enemy[pB] = union_parent(pA, enemy[pB]);
	}
	cout << 1;
}