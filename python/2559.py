import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = list(map(int, input().split()))
tempList = list(map(int, input().split()))
sumList = [tempList[0]] * N
for i in range(1, N):
    sumList[i] = sumList[i - 1] + tempList[i]
highScore = sumList[K - 1]

for i in range(1, N - K + 1):
    highScore = max(highScore, sumList[i + K - 1] - sumList[i - 1])

print(highScore)