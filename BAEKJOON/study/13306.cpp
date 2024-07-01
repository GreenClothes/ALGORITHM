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

int N, Q, org[200001], parent[200001], query[400001][3], x, b, c, d;
vector<string> ans;

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

    cin >> N >> Q;
    ans.reserve(Q);
    parent[1] = 1;
    org[1] = 1;
    for (int i = 2; i <= N; i++) {
        cin >> org[i];
        parent[i] = org[i];
    }

    for (int i = 0; i < N-1+Q; i++) {
        cin >> x;
        query[i][0] = x;
        if (x == 0) {
            cin >> b;
            query[i][1] = b;
            parent[b] = b;
        }
        else if (x == 1) {
            cin >> c >> d;
            query[i][1] = c;
            query[i][2] = d;
        }
    }

    for (int i = N + Q - 2; i >= 0; i--) {
        if (query[i][0] == 0) {
            union_parent(query[i][1], org[query[i][1]]);
        }
        else if (query[i][0] == 1) {
            if (find_parent(query[i][1]) == find_parent(query[i][2])) ans.push_back("YES");
            else ans.push_back("NO");
        }
    }

    while (!ans.empty()) {
        cout << ans.back() << '\n';
        ans.pop_back();
    }
}