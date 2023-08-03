import sys
sys.stdin = open("input.txt", "rt")
def Count(capacity):
    sum = 0
    cnt = 1
    for x in songs:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

N, M = map(int, input().split())
songs = list(map(int, input().split()))
s = 1
e = sum(songs)
res = 0
while s <= e:
    mid = (s+e)//2
    if Count(mid) <= M:
        res = mid
        e = mid-1
    else:
        s = mid+1

print(res)