from itertools import combinations
import sys
import math

def input():
    return sys.stdin.readline().rstrip()

T = int(input())


for _ in range(T):
    ans = float("inf")
    N = int(input())
    allX = 0
    allY = 0
    numList = [tuple() for _ in range(N)]
    for i in range(N):
        numList[i] = tuple(map(int, input().split()))
        allX += numList[i][0]
        allY += numList[i][1]
    C = list(combinations(numList, int(N / 2)))
    for i in range(len(C)):
        dx = 0
        dy = 0
        for j in range(int(N / 2)):
            dx += C[i][j][0]
            dy += C[i][j][1]
        ans = min(math.sqrt((dx * 2 - allX) ** 2 + (dy * 2 - allY) ** 2), ans)
    print(ans)