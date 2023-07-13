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
# num[::-1] <- 입력 받은 수를 거꾸로 뒤집음.