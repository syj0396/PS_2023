import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
maxi = -2147000000
for i in range(N):
    n1, n2, n3 = map(int, input().split())
    if n1 == n2 and n2 == n3:
        money = 10000 + n1 * 1000
    elif n1 == n2 or n1 == n3:
        money = 1000 + n1 * 100
    elif n2 == n3:
        money = 1000 + n2 * 100
    else:
        money = max(n1, n2, n3) * 100
    if money > maxi:
        maxi = money
print(maxi)