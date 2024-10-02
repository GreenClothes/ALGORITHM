#include<iostream>
#include<cstring>
#include<queue>
#include<algorithm>

using namespace std;

int N, An[1000000], res[1000000], big_loc[1000000], maxnum;

void find_NGE(int now, int next) {
	if (An[now] < An[next]) {
		res[now] = An[next];
		big_loc[now] = next;
		return;
	}
	else if (res[next] == -1) {
		res[now] = -1;
		big_loc[now] = -1;
		return;
	}
	else if (An[now] >= An[next]) {
		find_NGE(now, big_loc[next]);
	}
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> An[i];
	}

	res[N - 1] = -1;
	big_loc[N - 1] = -1;

	for (int i = N - 2; i >= 0; i--) {
		find_NGE(i, i + 1);
	}

	for (int i = 0; i < N; i++) {
		cout << res[i] << ' ';
	}

	return 0;
}