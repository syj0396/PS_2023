input_str = input().upper()
dic = {s: 0 for s in input_str}
for s in input_str:
    dic[s] += 1
max_cnt = max(list(dic.values()))
cnt = 0
max_value = ""
for k in dic:
    if dic[k] == max_cnt:
        cnt += 1
        max_value = k
if cnt > 1:
    print("?")
else:
    print(max_value)