import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())
writtenCard = list(map(int, input().split()))
cardDict = dict()
for i in range(N):
    if writtenCard[i] in cardDict:
        cardDict[writtenCard[i]] += 1
    else:
        cardDict[writtenCard[i]] = 1
M = int(input())
targetCard = list(map(int, input().split()))
ans = [0] * M
for i in range(M):
    if targetCard[i] in cardDict:
        ans[i] = cardDict[targetCard[i]]
    else:
        ans[i] = 0

print(*ans)