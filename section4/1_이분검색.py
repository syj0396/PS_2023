import sys
#sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = 0
e = N-1

while s <= e:
    m = (s+e)//2
    if a[m] == M:
        print(m+1)
        break
    elif a[m] < M:
        s = m+1
    else:
        e = m-1