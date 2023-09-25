#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    int board[20][20] = {0};
    int dp[20][20] = {0};
    cin >> N;
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            cin >> board[i][j];
        }
    }
    dp[0][0] = board[0][0];
    /*for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i == 0 && j == 0) continue;
            int minEnergy = 20;
            if (j - 1 < 0) minEnergy = dp[i - 1][j];
            else if (i - 1 < 0) minEnergy = dp[i][j - 1];
            else minEnergy = min(dp[i - 1][j], dp[i][j - 1]);
            dp[i][j] = minEnergy + board[i][j];
        }
    }*/

    for (int i = 1; i < N; ++i)
    {
        dp[i][0] = dp[i - 1][0] + board[i][0];
        dp[0][i] = dp[0][i - 1] + board[0][i];
    }
    for (int i = 1; i < N; ++i)
    {
        for (int j = 1; j < N; ++j)
        {
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + board[i][j];
        }
    }

    cout << dp[N - 1][N - 1];
    return 0;
}