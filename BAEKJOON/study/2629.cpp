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

int N, weights[31], M, marbles[7], weights_sum, weight_dp[40001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

    cin >> N;
    for (int n = 0; n < N; n++) {
        cin >> weights[n];
        weights_sum += weights[n];
    }
    cin >> M;
    for (int m = 0; m < M; m++) {
        cin >> marbles[m];
    }

    weight_dp[0] = 1;
    for (int i = 0; i < N; i++) {
        for (int j = weights_sum; j >= 0; j--) {
            if (weight_dp[j]) weight_dp[j + weights[i]] = 1;
        }
        for (int j = 0; j <= weights_sum; j++) {
            if (weight_dp[j]) weight_dp[abs(j - weights[i])] = 1;
        }
    }

    for (int m = 0; m < M; m++) {
        if (weight_dp[marbles[m]] == 1) {
            cout << "Y" << " ";
        }
        else {
            cout << "N" << " ";
        }
    }
}