import sys
#sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
nArray = list(map(int, input().split()))

lt = 0
rt = 1
tot = nArray[0]
cnt = 0
while True:
    if tot < M:
        tot += nArray[rt]
        rt += 1
    elif tot == M:
        cnt += 1
        lt += 1
        rt = lt + 1
        tot = nArray[lt]
    else:
        lt += 1


''' 마지막 케이스 시간 초과
cnt = 0
for i in range(N):
    sum = 0
    j = i
    while sum < M and j < N:
        sum += nArray[j]
        if sum == M:
            cnt += 1
        j += 1
print(cnt)
'''