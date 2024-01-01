def turnAscii(s):
    return(ord(s) - 97)

howMany = int(input())
groupWord = 0

for _ in range(howMany):
    asciiCheck = [False] * 26
    lastCheck = [-1] * 26
    checkFlag = True
    wordAscii = list(map(turnAscii, input()))
    for i in range(len(wordAscii)):
        if asciiCheck[wordAscii[i]] and abs(lastCheck[wordAscii[i]] - i) > 1:
            checkFlag = False
            break
        asciiCheck[wordAscii[i]] = True
        lastCheck[wordAscii[i]] = i
    if checkFlag:
        groupWord += 1

print(groupWord)