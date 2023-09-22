#include <iostream>
using namespace std;

int main()
{
    int N;
    int linesNum[46] = {0};
    cin >> N;

    linesNum[1] = 1;
    linesNum[2] = 2;
    for (int i = 3; i <= N; ++i)
    {
        linesNum[i] = linesNum[i - 1] + linesNum[i - 2];
    }
    cout << linesNum[N];
    return 0;
}
