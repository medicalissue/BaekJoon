import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
moveList = list(map(int, input().split()))
dictList = list()
for i in range(N):
    dictList.append({i + 1: moveList[i]})
ansList = list()
point = 0

for _ in range(N):
    popBaloon = dictList.pop(point)
    movePointer = int(list(popBaloon.values())[0])
    ansList.append(int(list(popBaloon.keys())[0]))
    if movePointer > 0:
        point -= 1
    for _ in range(abs(movePointer)):
        if movePointer > 0:
            point += 1
        elif movePointer < 0:
            point -= 1
        
        if point == len(dictList):
            point = 0
        elif point == -1:
            point = len(dictList) - 1

print(*ansList)