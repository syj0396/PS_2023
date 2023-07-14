N = int(input())
word_list = []
for i in range(N):
    word_list.append(input())
word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=len)

for w in word_list:
    print(w)