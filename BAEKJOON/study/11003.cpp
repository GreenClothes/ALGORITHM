#include<iostream>
#include<cstring>
#include<queue>
#include<vector>
#include<algorithm>
#include<string>
#include<deque>
#include<unordered_map>

using namespace std;

int N, L, A[5000001];
deque<int> dq;

int main(int argc, char** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> L;
	for (int i = 1; i <= N; i++) {
		if(i >= L+1 && dq.front() == A[i - L]) dq.pop_front();
		cin >> A[i];
		while (!dq.empty() && dq.back() > A[i]) dq.pop_back();
		dq.push_back(A[i]);
		cout << dq.front() << " ";
	}

	return 0;
}