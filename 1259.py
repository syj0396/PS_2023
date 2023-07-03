while True:
    num = input()
    if num == "0":
        break
    numlen = len(num)
    breaked = False
    for i in range(numlen // 2):
        if num[i] != num[numlen-i-1]:
            breaked = True
            break
    if breaked:
        print("no")
    else:
        print("yes")