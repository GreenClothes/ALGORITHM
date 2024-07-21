#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>

using namespace std;

int N, blocks[1001];

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> N;
	blocks[1] = 1;
	blocks[2] = 3;
	for (int i = 3; i <= N; i++) {
		blocks[i] = (blocks[i - 1] + blocks[i - 2] * 2) % 10007;
	}

	cout << blocks[N];

	return 0;
}