import sys
input = sys.stdin.readline

N = int(input())
coordList = list(map(int, input().split()))
sortedList = sorted(list(set(coordList)))
ansList = [0] * N
dictList = dict()
for i in range(len(sortedList)):
    dictList[sortedList[i]] = i
for i in range(N):
    ansList[i] = dictList[coordList[i]]

print(*ansList)