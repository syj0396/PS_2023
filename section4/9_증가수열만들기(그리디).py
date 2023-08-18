import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
nums = list(map(int, input().split()))
# 둘다 cur보다 작은 경우 break
# 둘다 cur보다 큰 경우, 둘 중 작은 쪽을 pop
# 한쪽만 cur보다 큰 경우, 그 쪽을 pop
cur = -1
str = ""
if nums[0] < nums[-1]:
    cur = nums[0]
    nums.pop(0)
    str += 'L'
else:
    cur = nums[-1]
    nums.pop()
    str += 'R'
cnt = 1
while nums:
    l = nums[0]
    r = nums[-1]
    if l < cur and r < cur:
        break
    if l > cur and r > cur:
        if l < r:
            cur = nums.pop(0)
            str += 'L'
        else:
            cur = nums.pop()
            str += 'R'
    elif l > cur:
        cur = nums.pop(0)
        str += 'L'
    else:
        cur = nums.pop()
        str += 'R'
    cnt += 1
print(cnt)
print(str)