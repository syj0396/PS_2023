import sys
#sys.stdin = open("input.txt", "rt")

def reverse(x):
    rv_str = ''
    for s in str(x):
        rv_str = s + rv_str
    return int(rv_str)

# 2부터 x까지의 수로 나누면서 나머지가 0이 되는게 있는지 확인하는게 빠른지
# 에라토스테네스 체로 다 계산해서 뽑는게 나은지.
# 첫번째 방법으로 하나의 수에 대해 하는건 두번째 방법과 동일?
def isPrime(x):
    if x == 1:
        return False
    #for i in range(2, x):
    for i in range(2, x//2+1): # 약수는 자신의 절반 이하로 존재할 수밖에 없음. 왜냐면 자신보다 작은 약수가 2 * _ 니까.
        if x % i == 0:
            return False
    return True

N = int(input())
nlist = list(map(int, input().split()))
for n in nlist:
    rv = reverse(n)
    if isPrime(rv):
        print(rv, end=' ')