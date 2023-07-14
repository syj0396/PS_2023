import sys

def digit_sum(x):
    sum = 0
    for s in str(x):
        sum += int(s)
    return sum
#or
'''
    while x > 0:
        sum += x % 10
        x = x // 10
'''


#sys.stdin = open("input.txt", "rt")
N = int(input())
N_list = list(map(int, input().split()))

max = -2147000000
maxN = -2147000000
for n in N_list:
    sum = digit_sum(n)
    if sum > max:
        max = sum
        maxN = n
print(maxN)