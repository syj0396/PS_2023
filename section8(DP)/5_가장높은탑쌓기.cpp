#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Node
{
    int area;
    int height;
    int weight;
};

bool cmpArea(Node n1, Node n2)
{
    return n1.area < n2.area;
}

bool cmpWeight(Node n1, Node n2)
{
    return n1.weight < n2.weight;
}

int main()
{
    int N;
    vector<Node> vec;
    int dp[100] = {0};
    int dp2[100] = {0};

    cin >> N;
    for (int i = 0; i < N; ++i)
    {
        int area, height, weight;
        cin >> area >> height >> weight;
        vec.push_back({area, height, weight});
    }

    sort(vec.begin(), vec.end(), cmpArea);
    dp[0] = vec[0].height;
    int totMax = dp[0];
    for (int i = 1; i < N; ++i)
    {
        int max = 0;
        for (int j = i - 1; j >= 0; --j)
        {
            if (vec[j].weight < vec[i].weight && dp[j] > max)
            {
                max = dp[j];
            }
        }
        dp[i] = max + vec[i].height;
        if (dp[i] > totMax)
            totMax = dp[i];
    }

    sort(vec.begin(), vec.end(), cmpWeight);
    dp2[0] = vec[0].height;
    for (int i = 1; i < N; ++i)
    {
        int max = 0;
        for (int j = i - 1; j >= 0; --j)
        {
            if (vec[j].area < vec[i].area && dp2[j] > max)
            {
                max = dp2[j];
            }
        }
        dp2[i] = max + vec[i].height;
        if (dp2[i] > totMax)
            totMax = dp2[i];
    }
    cout << totMax;
    return 0;
}