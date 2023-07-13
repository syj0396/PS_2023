import sys
#sys.stdin = open("input.txt", "rt")
T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    lists = list(map(int, input().split()))
    lists = lists[s-1:e]
    lists.sort() # sort() 함수는 반환값이 없기 때문에 독립적으로 사용. lists.sort()[k-1]은 오류!
    print('#%d %d' %(i+1, lists[k-1]))