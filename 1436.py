N = int(input())
list6 = []
for i in range(N):
    pre = int(str(i)+'666')
    post = int('666'+str(i))
    list6.append(pre)
    list6.append(post)
list6.sort()
print(list6[N-1])