import sys
#sys.stdin = open("input.txt", "rt")
K, N = map(int, input().split())

ls = []
maxv = -2147000000
for i in range(K):
    n = int(input())
    if n > maxv:
        maxv = n
    ls.append(n)
tot = 0
min_tot = maxv
min_val = maxv
s = 0
e = maxv
while s <= e:
    tot = 0
    mid = (s+e)//2
    for i in range(K):
        tot += ls[i] // mid
    if tot < N:
        e = mid - 1
    elif tot == N:
        min_val = mid
        break
    else:
        s = mid + 1

    if abs(N-tot) < min_tot:
        min_tot = tot
        min_val = mid
print(min_val)