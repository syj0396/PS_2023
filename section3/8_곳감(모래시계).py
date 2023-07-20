import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
for i in range(M):
    row, arrow, time = map(int, input().split())
    row -= 1
    if arrow == 0: #왼쪽 회전
        arr[row] = arr[row][time%N:] + arr[row][:time%N]
    else:
        arr[row] = arr[row][N-time%N:] + arr[row][:N-time%N]

s = 0
e = N-1
tot = 0
for i in range(N):
    for j in range(s, e+1):
        tot += arr[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(tot)