f = open('plaintext.txt', 'r', encoding='utf-8')
encryptedText = f.read()
alphabetList = list(set(encryptedText))
alphabetNumList = []
for i in set(encryptedText):
    num = encryptedText.count(i)
    alphabetNumList.append(num)

alphabetFreqDict = dict(zip(alphabetList, alphabetNumList))
alphabetFreqDict = sorted(alphabetFreqDict.items(), key=lambda x: x[1])
print(str(alphabetFreqDict))