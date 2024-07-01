#include <iostream>
#include <string.h>
using namespace std;

double A, B, AB[19][19][19];
bool isPrime[19];

double soccer(int idx, int a, int b) {
    // 최종 90분이 되었을 때 골이 소수로 들어갔는지 확인
    if (idx == 18) return isPrime[a] || isPrime[b] ? 1.0 : 0.0;
    // 이미 골이 소수로 들어갔는지 확인되었으면 더 이상 진행X (dp)
    if (AB[idx][a][b]) return AB[idx][a][b];
    
    AB[idx][a][b] += soccer(idx + 1, a + 1, b + 1) * A * B;
    AB[idx][a][b] += soccer(idx + 1, a + 1, b) * A * (1 - B);
    AB[idx][a][b] += soccer(idx + 1, a, b + 1) * (1 - A) * B;
    AB[idx][a][b] += soccer(idx + 1, a, b) * (1 - A) * (1 - B);
    return AB[idx][a][b];
}


int main() {
    cin >> A >> B;
    memset(isPrime, true, sizeof(isPrime));
    isPrime[0] = false;
    isPrime[1] = false;
    for (int i = 2; i < 19; i++) {
        if (isPrime[i]) {
            for (int j = i*2; j < 19; j+=i) {
                isPrime[j] = false;
            }
        }
    }

    A /= 100; B /= 100;
    printf("%.6lf", soccer(0, 0, 0));
}