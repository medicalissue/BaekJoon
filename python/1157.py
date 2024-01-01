def turnCapital(ch):
    if ch > 95:
        return ch - 32
    else:
        return ch

countAlpha = [0] * 26
howMany = 0
target = -1

originalAscii = list(map(ord, input()))
allCapAscii = list(map(turnCapital, originalAscii))

for i in range(len(allCapAscii)):
    countAlpha[allCapAscii[i] - 65] += 1

for i in range(len(countAlpha)):
    if countAlpha[i] == max(countAlpha):
        howMany += 1
        target = i + 65

if howMany > 1:
    print("?")
else:
    print(chr(target))