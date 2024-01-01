croaAlpabet = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]

word = input()
wordCount = 0

for i in range(len(word)):
    if i + 1 < len(word):
        tempWord = word[i] + word[i + 1]
    else:
        continue

    if tempWord in croaAlpabet:
        continue
    elif i + 2 < len(word) and tempWord + word[i + 2] == "dz=":
        continue
    wordCount += 1

wordCount += 1
print(wordCount)