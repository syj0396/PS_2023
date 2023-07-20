import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for a in arr:
    a.insert(0, 0)
    a.append(0)
arr.insert(0, [0]*(N+2))
arr.append([0]*(N+2))
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        n = arr[i][j]
        if n > arr[i-1][j] and n > arr[i+1][j] and n > arr[i][j-1] and n > arr[i][j+1]:
            cnt += 1
print(cnt)