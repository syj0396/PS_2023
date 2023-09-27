#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define costMax 21

int main()
{
    int N, M;
    int dp[101][101]; // dp[i][j]: i -> j로 가는 최소 비용

    cin >> N >> M;
    for (int i = 1; i <= N; ++i)
    {
        for (int j = 1; j <= N; ++j)
        {
            dp[i][j] = costMax;
        }
    }
    for (int i = 1; i <= N; ++i)
    {
        dp[i][i] = 0;
    }

    for (int i = 0; i < M; ++i)
    {
        int from, to, cost;
        cin >> from >> to >> cost;
        dp[from][to] = cost;
    }

    for (int n = 1; n <= N; ++n)
    {
        for (int i = 1; i <= N; ++i)
        {
            for (int j = 1; j <= N; ++j)
            {
                dp[i][j] = min(dp[i][j], dp[i][n] + dp[n][j]);
            }
        }
    }

    for (int i = 1; i <= N; ++i)
    {
        for (int j = 1; j <= N; ++j)
        {
            if (dp[i][j] >= costMax)
                cout << "M ";
            else
                cout << dp[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}