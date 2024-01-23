#include <iostream>
using namespace std;
#define endl "\n"

int N, tile[1001];

int whole_tile(int n) {
    if (n == 1) return 1;
    if (n == 2) return 3;
    if (tile[n] != 0) return tile[n];
    return tile[n] = whole_tile(n - 1) + 2 * whole_tile(n - 2);
}

int main() {
    cin >> N;
    tile[0] = 1;
    tile[1] = 1;
    tile[2] = 3;
    whole_tile(N);
    if (N % 2) {
        cout << (tile[N] + tile[(N - 1) / 2]) / 2 << endl;
    }
    else {
        cout << (tile[N] + tile[N / 2] + 2 * tile[N / 2 - 1]) / 2 << endl;
    }
}