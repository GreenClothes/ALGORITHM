// https://www.acmicpc.net/problem/1520
#include <iostream>
using namespace std;

int N, M, dr, dc;
int dy[] = { 0, 1, -1, 0 }, dx[] = { 1, 0, 0, -1 };
int map[500][500], map_dp[500][500] = { 0, };

int dfs(int y, int x) {
    if (y == M - 1 && x == N - 1) { return 1; }
    if (map_dp[y][x] != 0) { return map_dp[y][x]; }
    for (int i = 0; i < 4; i++) {
        dr = y + dy[i];
        dc = x + dx[i];

        if (dr >= 0 && dr < M && dc >= 0 && dc < N) {
            if (map[y][x] > map[dr][dc]) {
                map_dp[y][x] += dfs(dr, dc);
            }
        }
    }
    return map_dp[y][x];
}

int main() {
    cin >> M >> N;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
        }
    }
    cout << dfs(0, 0) << endl;
}