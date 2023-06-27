H, M = input().split()
H, M = int(H), int(M)
diff = M - 45
if diff < 0:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = 60 + diff
    print(H, M)
else:
    print(H, diff)