import sys
#sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
wages = list(map(int, input().split()))
wages.sort(reverse=True)
cnt = 0
cur = 0
cmp = N-1
while cur < cmp:
    if wages[cur] + wages[cmp] > M:
        cnt += 1
        cur += 1
    else:
        cnt += 1
        cur += 1
        cmp -= 1
if cur == cmp:
    cnt += 1
print(cnt)