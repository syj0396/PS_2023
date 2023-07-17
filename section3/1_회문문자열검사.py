import sys
#sys.stdin = open("input.txt", "rt")
N = int(input())
for i in range(N):
    circleStr = input().lower()
    length = len(circleStr)
    for j in range(length//2):
        if circleStr[j] != circleStr[length-1-j]: #or 우변을 circleStr[-1-j]
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

    #다른 방법:
    '''
    if circleStr == circleStr[::-1]:
        print("YES")
    else:
        print("NO")
    '''