import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

queue = 0
stack = 1
N = int(input())
isQorS = list(map(int, input().split()))
queuestack = list(map(int, input().split()))
queuedeck = deque()
M = int(input())
C = list(map(int, input().split()))
ansList = list()

for i in range(N):
    if isQorS[i] == queue:
        queuedeck.appendleft(queuestack[i])
for i in range(M):
    queuedeck.append(C[i])

queuedeck = list(queuedeck)[:M]
print(*queuedeck)