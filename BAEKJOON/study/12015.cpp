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

int N, input;
vector<int> v;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> input;
        if (v.size() == 0) {
            v.push_back(input);
        }
        else {
            if (v[v.size() - 1] < input) {
                v.push_back(input);
            }
            else {
                *(lower_bound(v.begin(), v.end(), input)) = input;
            }
        }
    }

    cout << v.size();
}