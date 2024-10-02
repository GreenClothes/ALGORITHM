#include<iostream>
#include<cstring>
#include<queue>
#include<algorithm>

using namespace std;

priority_queue<int, vector<int>, greater<>> pq;
int N, input, n1, n2, ans;

int main(int argc, char** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> input;
		pq.push(input);
	}

	while (pq.size() != 1) {
		n1 = pq.top();
		pq.pop();
		n2 = pq.top();
		pq.pop();

		ans += (n1 + n2);
		pq.push(n1 + n2);
	}

	cout << ans;

	return 0;
}