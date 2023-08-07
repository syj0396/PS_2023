import sys
#sys.stdin = open("input.txt", "rt")
def Count(length):
    cnt = 1
    prev = 0
    for i in range(1,N):
        if pos[i] - pos[prev] >= length:
            cnt += 1
            prev = i
    return cnt

N, C = map(int, input().split())
pos = []
for _ in range(N):
    pos.append(int(input()))
pos.sort()

lt = 1
rt = pos[N-1]
res = rt
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= C:
        lt = mid+1
        res = mid
    else:
        rt = mid-1
print(res)