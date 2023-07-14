N = int(input())
for i in range(N):
    inputs = input()
    score_list = []
    score = 0
    for s in inputs:
        if s == 'O':
            score += 1
        else:
            score = 0
        score_list.append(score)
    sum = 0
    for n in score_list:
        sum += n
    print(sum)
