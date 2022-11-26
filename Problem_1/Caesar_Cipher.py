caseNum = input()
numIter = 0
while numIter < int(caseNum):
    try:
        alphabet = input()
        plaintext = input()
        encryptString = input()
    except EOFError:
        break
    successShift = ""
    alphabetLen = len(alphabet)
    plaintextLen = len(plaintext)
    for shift in range(0, alphabetLen):
        txt = ""
        shiftAlphabet = ""
        if plaintextLen > len(encryptString):
            break
        if plaintextLen == 1:
            index = alphabet.find(plaintext[0])
            shiftAlphabetIndex = (index + shift) % alphabetLen
            txt = alphabet[shiftAlphabetIndex]
        else:

            for i in range(0, alphabetLen):
                shiftAlphabetIndex = (i + shift) % alphabetLen
                shiftAlphabet += alphabet[shiftAlphabetIndex]
            
            shiftAlphabetDict = plaintext.maketrans(alphabet,shiftAlphabet)
            txt = plaintext.translate(shiftAlphabetDict)

        plaintextIndex = encryptString.find(txt)
        if plaintextIndex != -1:
            startIndex = plaintextIndex + plaintextLen +1
            secondIndex = encryptString.find(txt,startIndex)
            if secondIndex == -1:
                successShift = successShift + " " + str(shift)

    if successShift == "":
        print("no solution")
    elif len(successShift) == 2:
        print("unique: " + str(successShift[1]))
    else:
        print("ambiguous:" + successShift)

    numIter += 1