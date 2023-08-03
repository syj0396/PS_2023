import sys
sys.stdin = open("input.txt", "rt")
def Counts(length):
    cnt = 0
    for x in lines:
        cnt += x//length
    return cnt
K, N = map(int, input().split())
max = 0
lines = []
for i in range(K):
    n = int(input())
    lines.append(n)
    if n > max:
        max = n
s = 1
e = max
res = 0
while s <= e:
    mid = (s+e)//2
    if Counts(mid) >= N:
        s = mid+1
        res = mid
    else:
        e = mid-1
print(res)