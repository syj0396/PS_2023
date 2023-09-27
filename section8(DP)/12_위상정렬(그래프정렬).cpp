#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    int N, M;
    vector<vector<int>> graph;
    vector<int> fromCnt = {0};
    queue<int> q;
    cin >> N >> M;
    graph.resize(N + 1);
    fromCnt.resize(N + 1);

    for (int i = 0; i < M; ++i)
    {
        int from, to;
        cin >> from >> to;
        graph[from].push_back(to);
        fromCnt[to]++;
    }
    for (int i = 1; i <= N; ++i)
    {
        if (fromCnt[i] == 0)
            q.push(i);
    }

    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (auto it = graph[node].begin(); it != graph[node].end(); ++it)
        {
            fromCnt[*it]--;
            if (fromCnt[*it] == 0)
                q.push(*it);
        }
    }
    return 0;
}