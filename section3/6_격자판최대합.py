import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
nArray = []
# nArray = [list(map(int, input().split())) for _ in range(N)]
max = -2147000000
for i in range(N):
    a = list(map(int, input().split()))
    nArray.append(a)
    if sum(a) > max:
        max = sum(a)

'''
for i in range(N):
    for j in range(N):
        sum1 += nArray[i][j]
        sum2 += nArray[j][i]
'''

for i in range(N):
    tot = 0
    for a in nArray:
        tot += a[i]
    if tot > max:
        max = tot

tot = 0
tot2 = 0
for i in range(N):
    tot += nArray[i][i]
    tot2 += nArray[i][N-i-1] # 다른 대각선!!!!!
if tot > max:
    max = tot
if tot2 > max:
    max = tot
print(max)