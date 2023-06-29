T = int(input())
for i in range(T):
    H, W, N = input().split()
    H, W, N = int(H), int(W), int(N)
    f1 = N % H
    el = N // H + 1
    if (f1 == 0):
        f1 = H
        el -= 1
    print(f1 * 100 + el)