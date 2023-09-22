#include <iostream>
using namespace std;

int main()
{
    int N;
    int arr[1000];
    int dp[1000] = {0};
    cin >> N;
    for (int i = 0; i < N; ++i)
    {
        cin >> arr[i];
    }
    dp[0] = 1;
    for (int i = 1; i < N; ++i)
    {
        int max = 0;
        for (int j = i - 1; j >= 0; --j)
        {
            if (arr[j] < arr[i] && dp[j] > max)
                max = dp[j];
        }
        dp[i] = max + 1;
    }

    int totMax = 0;
    for (int i = 0; i < N; ++i)
    {
        if (dp[i] > totMax)
            totMax = dp[i];
    }
    cout << totMax;
    return 0;
}