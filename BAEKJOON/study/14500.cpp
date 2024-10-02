#include<iostream>
#include<cstring>
#include<queue>
#include<algorithm>

using namespace std;

int N, M, nums[500][500], ans;

int type11(int y, int x) {
	if (x >= M - 3) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y][x + 2] + nums[y][x + 3];
}

int type12(int y, int x) {
	if (y >= N - 3) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y + 2][x] + nums[y + 3][x];
}

int type21(int y, int x) {
	if (y >= N - 1 || x >= M - 1) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y][x + 1] + nums[y + 1][x + 1];
}

int type31(int y, int x) {
	if (y >= N - 2 || x >= M - 1) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y + 2][x] + nums[y + 2][x + 1];
}

int type32(int y, int x) {
	if (y == 0 || x >= M - 2) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y][x + 2] + nums[y - 1][x + 2];
}

int type33(int y, int x) {
	if (y >= N - 2 || x >= M - 1) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y + 1][x + 1] + nums[y + 2][x + 1];
}

int type34(int y, int x) {
	if (y >= N - 1 || x >= M - 2) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y][x + 2] + nums[y + 1][x];
}

int type35(int y, int x) {
	if (y >= N - 2 || x >= M - 1) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y + 1][x] + nums[y + 2][x];
}

int type36(int y, int x) {
	if (y >= N - 1 || x >= M - 2) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y][x + 2] + nums[y + 1][x + 2];
}

int type37(int y, int x) {
	if (y >= N - 2 || x == 0) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y + 2][x] + nums[y + 2][x - 1];
}

int type38(int y, int x) {
	if (y >= N - 1 || x >= M - 2) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y + 1][x + 1] + nums[y + 1][x + 2];
}

int type41(int y, int x) {
	if (y >= N - 2 || x >= M - 1) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y + 1][x + 1] + nums[y + 2][x + 1];
}

int type42(int y, int x) {
	if (y == 0 || x >= M - 2) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y - 1][x + 1] + nums[y - 1][x + 2];
}

int type43(int y, int x) {
	if (y >= N - 2 || x == 0) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y + 1][x - 1] + nums[y + 2][x - 1];
}

int type44(int y, int x) {
	if (y >= N - 1 || x >= M - 2) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y + 1][x + 1] + nums[y + 1][x + 2];
}

int type51(int y, int x) {
	if (y >= N - 1 || x >= M - 2) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y + 1][x + 1] + nums[y][x + 2];
}

int type52(int y, int x) {
	if (y >= N - 2 || x >= M - 1) return 0;
	return nums[y][x] + nums[y + 1][x] + nums[y + 1][x + 1] + nums[y + 2][x];
}

int type53(int y, int x) {
	if (y == 0 || x >= M - 2) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y - 1][x + 1] + nums[y][x + 2];
}

int type54(int y, int x) {
	if (y == 0 || y >= N - 1 || x >= M - 1) return 0;
	return nums[y][x] + nums[y][x + 1] + nums[y - 1][x + 1] + nums[y + 1][x + 1];
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> nums[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			ans = max(ans, type11(i, j));
			ans = max(ans, type12(i, j));
			ans = max(ans, type21(i, j));
			ans = max(ans, type31(i, j));
			ans = max(ans, type32(i, j));
			ans = max(ans, type33(i, j));
			ans = max(ans, type34(i, j));
			ans = max(ans, type35(i, j));
			ans = max(ans, type36(i, j));
			ans = max(ans, type37(i, j));
			ans = max(ans, type38(i, j));
			ans = max(ans, type41(i, j));
			ans = max(ans, type42(i, j));
			ans = max(ans, type43(i, j));
			ans = max(ans, type44(i, j));
			ans = max(ans, type51(i, j));
			ans = max(ans, type52(i, j));
			ans = max(ans, type53(i, j));
			ans = max(ans, type54(i, j));
		}
	}

	cout << ans;

	return 0;
}