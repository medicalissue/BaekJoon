timeTable = "33344455566677788889990000"

def minusAscii(n):
    return n - 65

def getTime(n):
    if timeTable[n] == "0":
        return 10
    else:
        return int(timeTable[n])

word = list(map(ord, input()))
asciiList = list(map(minusAscii, word))
allTime = list(map(getTime, asciiList))
print(sum(allTime))