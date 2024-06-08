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

struct JEWEL {
	int m, v;

	bool operator<(JEWEL right) const {
		if (m < right.m) return true;
		return false;
	}
};
int N, K, idx;
long long C[300000], ans;
JEWEL jewel[300001];
priority_queue<int> bag;


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> jewel[i].m >> jewel[i].v;
	}
	for (int i = 0; i < K; i++) {
		cin >> C[i];
	}
	
	sort(jewel, jewel + N);
	sort(C, C + K);
	for (int i = 0; i < K; i++) {
		while (idx < N && C[i] >= jewel[idx].m) {
			bag.push(jewel[idx].v);
			idx++;
		}
		if (!bag.empty()) {
			ans += bag.top();
			bag.pop();
		}
	}
	cout << ans;
}