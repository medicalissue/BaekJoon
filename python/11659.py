import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = list(map(int, input().split()))
numList = list(map(int, input().split()))
sumList = [numList[0]] * N
for i in range(1, N):
    sumList[i] = sumList[i - 1] + numList[i]

for r in range(M):
    i, j = list(map(int, input().split()))
    if i != 1:
        print(sumList[j - 1] - sumList[i - 2])
    else:
        print(sumList[j - 1])