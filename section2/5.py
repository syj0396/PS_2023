N, M = map(int, input().split())
'''
sum_list = {x:0 for x in range(2, N+M+1)}
for i in range(1, N+1):
    for j in range(1, M+1):
        sum_list[i+j] += 1
max = max(list(sum_list.values()))
for k in sum_list:
    if sum_list[k] == max:
        print(k, end=' ')
'''
# dic의 key가 정수일 경우, 배열로 대체.
# key를 배열의 index로, value를 원소로.
cnt = [0]*(N+M+3)
max = -2147000000
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1
for i in range(N+M+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(N+M+1):
    if cnt[i] == max:
        print(i, end=' ')