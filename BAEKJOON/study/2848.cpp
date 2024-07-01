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

int N, alpha[27], alpha_num;
string str[101];
unordered_map<char, int> degree;
unordered_map<char, vector<char>> v;
queue<char> q, ans;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> str[i];
		for (int s = 0; s < str[i].size(); s++) {
			if (alpha[str[i][s] - 'a'] == 0) alpha_num++;
			alpha[str[i][s] - 'a'] = 1;
		}
	}

	int num = 0, idx = 0;
	while (num < N-1) {
		int alen = str[num].length(), blen = str[num + 1].length();
		int slen = alen < blen ? alen : blen;
		while (str[num][idx] == str[num + 1][idx] && idx < slen) idx++;
		if (idx != slen) {
			degree[str[num + 1][idx]]++;
			v[str[num][idx]].push_back(str[num + 1][idx]);
		}
		num++;
		idx = 0;
	}

	for (int i = 0; i < 26; i++) {
		if (alpha[i] && degree[char(i+'a')] == 0) {
			q.push(char(i + 'a'));
		}
	}

	int flg = 1;

	for (int i = 0; i < alpha_num; i++) {
		if (q.size() > 1) {
			flg = 0;
		}
		if (q.empty()) {
			cout << "!\n";
			return 0;
		}

		char qp = q.front();
		q.pop();
		ans.push(qp);
		for (char next : v[qp]) {
			degree[next]--;
			if (degree[next] == 0) {
				q.push(next);
			}
		}
	}

	if (flg) {
		while (!ans.empty()) {
			cout << ans.front();
			ans.pop();
		}
	}
	else {
		cout << "?\n";
	}
}