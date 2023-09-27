#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N, totTime;
    int dp[1001] = {0}; // dp[i]: 제한 시간이 i일 때 최대 점수
    cin >> N >> totTime;
    for (int i = 0; i < N; ++i)
    {
        int score, time;
        cin >> score >> time;
        for (int j = totTime; j >= time; --j)
        {
            dp[j] = max(dp[j], dp[j - time] + score);
        }
    }
    cout << dp[totTime];
    return 0;
}