N = int(input())
NList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))

'''
sort() 함수는 nlogn의 시간 복잡도
이 문제는 두 리스트가 정렬되어 있으므로, n의 시간 복잡도로 해결 가능.
'''
NMList = []
i, j = 0, 0
while i < N and j < M:
    if NList[i] < MList[j]:
        NMList.append(NList[i])
        i += 1
    else:
        NMList.append(MList[j])
        j += 1
if i == N:
    NMList += MList[j:]
else:
    NMList += NList[i:]
for x in NMList:
    print(x, end=' ')