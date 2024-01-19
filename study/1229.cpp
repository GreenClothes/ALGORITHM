// https://www.acmicpc.net/problem/1229
#include <iostream>
using namespace std;

int n = 1, idx = 0, N, six[1000001];

int main() {
    cin >> N;
    for (int i = 0; i <= N; i++) {
        six[i] = 6;
    }
    six[0] = 0;
    six[1] = 1;
    while (n <= N) {
        for (int i = n; i <= N; i++) {
            if (six[i] > six[i - n] + 1) {
                six[i] = six[i - n] + 1;
            }
        }
        n += 5 + 4 * idx;
        idx++;

    }
    cout << six[N] << endl;
}