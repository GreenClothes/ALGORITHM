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

int K, N, A[1000001], Q, a, b, parent[1000001], nearL[1000001], nearR[1000001], cnt[1000001];
long long ans;

int find_near(int a) {
	if (a == parent[a]) return a;
	return parent[a] = find_near(parent[a]);
}

void union_near(int a, int b) {
	int pa = find_near(a), pb = find_near(b);
	if (A[pa] == A[pb]) {
		if (pa < pb) {
			parent[pb] = pa;
			cnt[pa] += cnt[pb];
		}
		else if (pb < pa) {
			parent[pa] = pb;
			cnt[pb] += cnt[pa];
		}
	}
}

void del_near(int a) {
	int pa = find_near(a);
	cnt[pa] -= 1;

	int aL = nearL[a], aR = nearR[a];
	nearL[aR] = aL;
	nearR[aL] = aR;

	if (aL != 0 && aR != 0) union_near(aL, aR);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> K >> N;
	for (int i = 1; i <= N; i++) {
		parent[i] = i;
		nearL[i] = i - 1;
		nearR[i] = i + 1;
		cnt[i] = 1;
	}
	nearL[1] = 0;
	nearR[N] = 0;

	for (int i = 1; i <= N; i++) {
		cin >> A[i];
		union_near(i, i-1);
	}

	cin >> Q;
	for (int i = 0; i < Q; i++) {
		cin >> a >> b;
		if (a == 1) {
			del_near(b);
		}
		else if (a == 2) {
			ans += cnt[find_near(b)];
		}
	}
	cout << ans;
}