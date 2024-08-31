#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v;
unordered_map<int, int> um;
int n, q, input;

int main(int argc, char** argv)
{
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> input;
        v.push_back(input);
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < n; i++) {
        um[v[i]] = i;
    }

    for (int i = 0; i < n; i++) {
        cin >> input;
        if (um.find(input) == um.end()) {
            cout << "0\n";
        }
        else {
            int idx = um[input];
            cout << idx * (n - idx - 1) << '\n';
        }
    }

    return 0;
}