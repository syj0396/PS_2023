#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define costMax 55

int main()
{
    int N;
    int dp[51][51];
    int eachMax[51] = {0};
    int totMin = costMax;
    int cnt = 1;

    cin >> N;

    for (int i = 1; i <= N; ++i)
    {
        for (int j = 1; j <= N; ++j)
        {
            dp[i][j] = costMax;
        }
    }
    for (int i = 1; i < N; ++i)
    {
        dp[i][i] = 0;
    }

    while (1)
    {
        int from, to;
        cin >> from >> to;
        if (from == -1 && to == -1)
            break;
        dp[from][to] = 1;
        dp[to][from] = 1;
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
        int max = 0;
        for (int j = 1; j <= N; ++j)
        {
            if (dp[i][j] != costMax && dp[i][j] > max)
                max = dp[i][j];
        }
        eachMax[i] = max;
        if (max < totMin)
        {
            totMin = max;
            cnt = 1;
        }
        else if (max == totMin)
            cnt++;
    }

    cout << totMin << " " << cnt << endl;

    for (int i = 1; i <= N; ++i)
    {
        if (eachMax[i] == totMin)
            cout << i << " ";
    }
    return 0;
}