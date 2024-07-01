#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <climits>
#include <cmath>
#include <unordered_map>
using namespace std;

int N, K, c1, c2, tree[2000001], input;
char comm;

void init() {
	for (int n = N - 1; n > 0; n--) tree[n] = tree[n << 1] * tree[n << 1 | 1];
}

void update(int loc, int val) {
	for (tree[loc += N] = val; loc > 1; loc >>= 1) tree[loc >> 1] = tree[loc] * tree[loc ^ 1];
}

void query(int l, int r) {
	long long mul = 1;
	for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
		if (l & 1) mul *= tree[l++];
		if (r & 1) mul *= tree[--r];
	}
	if (mul > 0) cout << '+';
	else if (mul < 0) cout << '-';
	else cout << '0';
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	auto& is = std::cin;
	bool first = true;

	while (cin >> N >> K) {
		if (!first) cout << '\n';
		else first = false;

		memset(tree, 0, sizeof(tree));
		for (int n = N; n < 2 * N; n++) {
			cin >> input;
			if (input != 0) tree[n] = input / abs(input);
			else tree[n] = 0;
		}
		init();
		for (int k = 0; k < K; k++) {
			cin >> comm >> c1 >> c2;
			if (comm == 'C') {
				if (c2 != 0) c2 /= abs(c2);
				update(c1 - 1, c2);
			}
			else if (comm == 'P') {
				query(c1 - 1, c2);
			}
		}
	}
}