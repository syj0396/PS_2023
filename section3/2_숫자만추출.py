s = input()
num = ''
for x in s:
    if ord(x) >= ord('0') and ord(x) <= ord('9'):
        # 고민 1) 자연수로 만드는 방법
        # - 일단 string으로 만들고 int로 변환할 것인가 or
        # - int로 변환 후 10 * cnt + num해서 만들고 뒤집을 것인가
        # - str을 뒤집고 10 * cnt + num
        num += x #1번 방법
'''
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
'''
num = int(num)
print(num) 

numy = 2
for i in range(2, num//2+1):
    if num%i == 0:
        numy += 1
print(numy)