import sys
#sys.stdin = open("input.txt", "rt")
N, K = map(int, input().split())
lists = list(map(int, input().split()))
sum_lists = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = lists[i]+lists[j]+lists[k]
            sum_lists.append(sum)
uniq_list = list(set(sum_lists))
uniq_list.sort(reverse=True)
print(uniq_list[K-1])

