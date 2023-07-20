import sys
#sys.stdin = open("input.txt", "rt")
arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(7):
        if j < 3 and arr[i][j] == arr[i][j+4] and arr[i][j+1] == arr[i][j+3]:
            cnt += 1
        if i < 3 and arr[i][j] == arr[i+4][j] and arr[i+1][j] == arr[i+3][j]:
            cnt += 1
print(cnt)
