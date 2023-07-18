import sys
#sys.stdin = open("input.txt")
cList = list(range(1, 21))
#위에서 그냥 range(21) 하면 0 ... 21이 생성되어, 인덱스 접근할 때 -1 안해줘도 됨.
for i in range(10):
    a, b = map(int, input().split())
    for i in range((b-a)//2+1):
        temp = cList[a+i-1] #swap 방법: cList[a+i-1], cList[b-i-1] = cList[b-i-1], cList[a+i-1]
        cList[a+i-1] = cList[b-i-1]
        cList[b-i-1] = temp
for c in cList:
    print(c, end=' ')
