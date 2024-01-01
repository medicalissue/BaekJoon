import sys
input = sys.stdin.readline
N = int(input())
numList = [0] * N
for i in range(N):
    numList[i] = int(input())
print(*sorted(numList), sep = "\n")