while True:
    try:
        encryptText = input()
        originText = input()
    except EOFError:
        break

    encryptAlphabetArr = []
    originAlphabetArr = []
    for i in set(encryptText):
        num = encryptText.count(i)
        encryptAlphabetArr.append(num)

    for i in set(originText):
        num = originText.count(i)
        originAlphabetArr.append(num)

    encryptAlphabetArr.sort()
    originAlphabetArr.sort()

    if encryptAlphabetArr == originAlphabetArr:
        print("YES")
    else:
        print("NO")