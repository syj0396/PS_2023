import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

tot = 0
for i in range((N+1)//2 - 1):
    blank = N//2 - i #2 1
    for j in range(blank, N - blank):
        tot += a[i][j]
        tot += a[N-i-1][j]

for i in range(N):
    tot += a[N//2][i]

print(tot)