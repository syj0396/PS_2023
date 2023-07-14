N = int(input())
not_prime = [0]*(N+1)
cnt = 0
for i in range(2, N+1):
    if not_prime[i] == 0:
        cnt += 1
        for j in range(i+i, N+1, i):
            not_prime[j] = 1
print(cnt)