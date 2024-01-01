N = int(input())
numList = [0] * N
numList = list(map(int, input().split()))
primeCount = 0

for i in range(N):
    isPrime = True
    if numList[i] == 1:
        continue
    elif numList[i] == 2:
        primeCount += 1
        continue
    for j in range(2, numList[i]):
        if numList[i] % j == 0:
            isPrime = False
    if isPrime:
        primeCount += 1

print(primeCount)