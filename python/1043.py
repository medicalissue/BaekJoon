import sys
sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))
whoKnowsLie = list(map(int, input().split()))
whoKnowsLie.pop(0)

partyList = [0 for _ in range(M)]

cnt = 0

def dfs(n):
    for i in range(M):
        if n in partyList[i]:
            partyList[i].remove(n)
            partyList[i].append("*")
            for j in range(len(partyList[i])):
                if partyList[i][j] == "*":
                    continue
                dfs(partyList[i][j])

for i in range(M):
    tempList = list(map(int, input().split()))
    tempList.pop(0)
    partyList[i] = tempList

for i in whoKnowsLie:
    dfs(i)

for i in range(len(partyList)):
    if "*" in set(partyList[i]):
        continue
    cnt += 1

print(cnt)

