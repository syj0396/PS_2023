import sys
sys.stdin = open('input.txt', 'rt')
L = int(input())
boxes = list(map(int, input().split()))
cnt = int(input())

for i in range(cnt):
    boxes[0] -= 1
    boxes[L-1] += 1
    boxes.sort(reverse=True)
print(boxes)
print(boxes[0]-boxes[L-1])