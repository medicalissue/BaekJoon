import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
curLine = deque(map(int, input().split()))
sideLine = deque()
yesFlag = True

for i in range(1, N + 1):
    nonoFlag = True
    while True:
        if curLine and curLine[0] == i:
            curLine.popleft()
            nonoFlag = False
            break
        elif sideLine and sideLine[0] == i:
            sideLine.popleft()
            nonoFlag = False
            break
        elif curLine:
            sideLine.appendleft(curLine.popleft())

        if not curLine:
            break

    if nonoFlag:
        yesFlag = False
        print("Sad")
        break

if yesFlag:
    print("Nice")