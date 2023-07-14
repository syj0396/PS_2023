N, M = input().split()
N, M = int(N), int(M)
board = []
for i in range(N):
    strings = input()
    board.append(strings)

min = 10000
start_W = 'WBWBWBWB'
start_B = 'BWBWBWBW'
for i in range(N-8+1):
    for j in range(M-8+1):
        color = board[i][j]
        sum = 0
        for k in range(i, i+8):
            for t in range(j, j+8):
                if board[k][t] != color:
                    sum += 1
                if t != j+7:
                    if color == 'W':
                        color = 'B'
                    else:
                        color = 'W'
        if sum < min:
            min = sum

print(min)
