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

int TC, N, M, dp[11][1025], ans;
string str[11];
vector<pair<int, int>> v;

bool is_far(int bit) {
    for (int i = 0; i < M - 1; i++) {
        int check = 3 << i;
        if ((check & bit) == check) return false;
    }
    return true;
}

bool check_seat(int sit, int row) {
    for (int i = 0; i < M; i++) {
        if (str[row][i] == '.') continue;
        if (1 << (M - i - 1) & sit) return false;
    }
    return true;
}

bool check_front(int f_sit, int b_sit) {
    for (int bit = 1; bit < (1 << M); bit <<= 1) {
        if (b_sit & bit) {
            if (f_sit & (bit << 1)) return false;
            if (f_sit & (bit >> 1)) return false;
        }
    }
    return true;
}

void init() {
    ans = 0;
    v.clear();
    memset(dp, 0, sizeof(dp));
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> TC;
    for (int tc = 0; tc < TC; tc++) {
        init();
        cin >> N >> M;
        for (int i = 1; i <= N; i++) {
            cin >> str[i];
        }

        for (int bit = 0; bit < (1 << M); bit++) {
            if (is_far(bit)) {
                int man = 0;
                for (int i = 0; i < M; i++) {
                    if ((1 << i) & bit) man++;
                }
                v.push_back(make_pair(bit, man));
            }
        }

        for (int n = 1; n <= N; n++) {
            for (auto pii : v) {
                if (not check_seat(pii.first, n)) continue;
                for (auto f_seat : v) {
                    if (not check_front(pii.first, f_seat.first)) continue;
                    dp[n][pii.first] = max(dp[n][pii.first], pii.second + dp[n - 1][f_seat.first]);
                    ans = max(ans, dp[n][pii.first]);
                }
            }
        }

        cout << ans << '\n';
    }
}