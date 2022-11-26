f = open('plaintext.txt', 'r', encoding='utf-8')
encryptedText = f.read()


encryptList = []
alphabet = []
for i in range(97,123):
    subAscii = i+6
    if subAscii > 122:
        subAscii = subAscii - 26
    subAlphabet = chr(subAscii)
    encryptList.append(subAlphabet)

for i in range(97,123):
    alphabet.append(chr(i))


substitutionDict = dict(zip(alphabet, encryptList))
# print(str(substitutionDict))


transTable = encryptedText.maketrans(substitutionDict)
txt = encryptedText.translate(transTable)
f = open('decryptedText2.txt','w')
f.write(txt)
# print(txt)