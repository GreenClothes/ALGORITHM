#include <iostream>
#include <map>
using namespace std;
# define endl "\n"

map<long long, long long> dp;
long long N, P, Q;

long long find(long long n) {
    if (dp.find(n) != dp.end()) {
        return dp[n];
    }

    long long temp;
    temp = find(n / P) + find(n / Q);
    dp[n] = temp;
    return temp;
}

int main() {
    cin >> N >> P >> Q;

    dp[0] = 1;
    if (N == 0) {
        cout << 1 << endl;
    }
    else {
        cout << find(N) << endl;
    }
}