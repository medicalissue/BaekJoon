import sys

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
numList = list()
for _ in range(N):
    numList.append(int(input()))
sortList = sorted(numList)
modeDict = dict()
lastNumCnt = 1

print(round(sum(numList) / len(numList)))
print(sortList[int((len(sortList) / 2))])
for i in range(N - 1):
    if sortList[i] == sortList[i + 1]:
        lastNumCnt += 1
        if i == N - 2:
            modeDict[sortList[i]] = lastNumCnt
    else:
        modeDict[sortList[i]] = lastNumCnt
        lastNumCnt = 1
        if i == N - 2:
            modeDict[sortList[i + 1]] = lastNumCnt

if len(numList) != 1:
    hiscore = [k for k,v in modeDict.items() if max(modeDict.values()) == v]
else:
    hiscore = numList
if len(hiscore) > 1:
    print(hiscore[1])
else:
    print(hiscore[0])
print(max(numList) - min(numList))