length = int(input())
numList = list(map(int, input().split()))
highScore = -1000001
lowScore = 1000001

for i in range(length):
    highScore = max(highScore, numList[i])
    lowScore = min(lowScore, numList[i])

print(str(lowScore) + " " + str(highScore))