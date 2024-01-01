N = int(input())
numList = [0] * N
for i in range(N):
    numList[i] = int(input())

for _ in range(N - 1):
    for i in range(N - 1):
        if numList[i] > numList[i + 1]:
            numList[i], numList[i + 1] = numList[i + 1], numList[i]

print(*numList, sep = "\n")