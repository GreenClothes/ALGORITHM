#include<iostream>
#include<cstring>
#include<queue>
#include<algorithm>

using namespace std;

vector<int> v;
int N, C, x;

int main(int argc, char** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> C;
	for (int i = 0; i < N; i++) {
		cin >> x;
		v.push_back(x);
	}
	sort(v.begin(), v.end());

	int start = 1, end = v[N - 1] - v[0];
	int res = 0;

	while (start <= end) {
		int mid = (start + end) / 2;

		int cnt = 1;
		int prev = v[0];
		for (int i = 1; i < N; i++) {
			if (v[i] - prev >= mid) {
				prev = v[i];
				cnt++;
			}
		}

		if (cnt >= C) {
			res = max(res, mid);
			start = mid + 1;
		}
		else {
			end = mid - 1;
		}
	}

	cout << res;

	return 0;
}