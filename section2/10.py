import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
answers = list(map(int, input().split()))
total_score = 0
score = 1
for a in answers:
    if a == 1:
        total_score += score
        score += 1
    else:
        score = 1
print(total_score)