import sys
sys.stdin = open('input.txt', 'rt')
N = int(input())
players = []
for i in range(N):
    k, m = map(int, input().split())
    players.append((k, m))
players.sort(reverse=True)

cnt = 0
maxx = 0
for _, m in players:
    if m > maxx:
        cnt += 1
        maxx = m
print(cnt)