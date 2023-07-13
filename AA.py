import sys
#sys.stdin = open("input.txt", "rt")
num, nth = map(int, input().split())
yak = []
for i in range(1, num+1):
    if num % i == 0:
        yak.append(i)
if nth <= len(yak):
    print(yak[nth-1])
else:
    print(-1)