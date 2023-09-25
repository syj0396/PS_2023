#include <iostream>
#include <vector>
using namespace std;

vector<int> dp = {0}; // dp[i]: 가방 무게가 i일 때 최대 가치

int main()
{
    int N, totWeight;
    cin >> N >> totWeight;
    dp.resize(totWeight + 1);

    for (int i = 0; i < N; ++i)
    {
        int weight, value;
        cin >> weight >> value;
        for (int j = weight; j <= totWeight; ++j)
        {
            dp[j] = max(dp[j], dp[j - weight] + value);
        }
    }
    cout << dp[totWeight];
    return 0;
}