import sys
import math

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
treeList = [0] * N
for i in range(N):
    treeList[i] = int(input())
ans = 0

minusList = [0] * (N - 1)
for i in range(N - 1):
    minusList[i] = treeList[i + 1] - treeList[i]

width = math.gcd(minusList[0], minusList[1])
for i in range(2, N - 1):
    width = math.gcd(width, minusList[i])

for i in range(N - 1):
    ans += minusList[i] / width - 1

print(int(ans))