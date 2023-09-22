#include <iostream>
using namespace std;

int methodNum[47] = {0};
void dfs(int n)
{
    if (n == 0 || n == 1)
    {
        methodNum[n] = n + 1;
        return;
    }
    if (methodNum[n - 1] == 0)
        dfs(n - 1);
    if (methodNum[n - 2] == 0)
        dfs(n - 2);
    methodNum[n] = methodNum[n - 1] + methodNum[n - 2];
    return;
}
int main()
{
    int N;
    cin >> N;
    dfs(N);
    cout << methodNum[N];
    return 0;
}