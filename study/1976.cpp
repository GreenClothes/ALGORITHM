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

int N, M, input, parent[201];

int find_parent(int a) {
    if (a == parent[a]) return a;
    return parent[a] = find_parent(parent[a]);
}

void union_parent(int a, int b) {
    a = find_parent(a);
    b = find_parent(b);

    if (a == b) return;

    if (a < b) {
        parent[b] = a;
    }
    else if (a > b) {
        parent[a] = b;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        parent[i] = i;
    }
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> input;
            if (input) {
                union_parent(i, j);
            }
        }
    }
    cin >> input;
    int temp_parent = find_parent(input), next_parent, flg = 1;
    for (int i = 0; i < M - 1; i++) {
        cin >> input;
        next_parent = find_parent(input);
        if (next_parent != temp_parent) flg = 0;
    }

    if (flg) cout << "YES";
    else cout << "NO";
}