import sys
sys.stdin = open("input.txt", "rt")
N = int(input())
scores = list(map(int, input().split()))
#avg = round(sum(scores) / N, 0)
# round는 round_half_even 방식을 택함. 4.5이면 짝수로, 즉 4가 되어버림.
# 따라서, 0.5를 더하고 int 씌워주기
avg = sum(scores) / N + 0.5
avg = int(avg)
min_diff = 100
min_score = 100
min_std = N
for i, x in enumerate(scores):
    diff = abs(avg - x)
    if diff < min_diff:
        min_diff = diff
        min_score = x
        min_std = i
    elif diff == min_diff:
        if x > min_score: #만약 >= 였다면, 동점 중 가장 나중의 학생.
            min_score = x
            min_std = i
print(int(avg), min_std+1)