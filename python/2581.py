M = int(input())
N = int(input())
primeSum = 0
min = 0
isFirst = True

for i in range(M, N + 1):
    isPrime = True
    if i == 1:
        continue
    elif i == 2:
        primeSum += i
        if isFirst:
            min = i
            isFirst = False
        continue
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if isPrime:
        primeSum += i
        if isFirst:
            min = i
            isFirst = False

if primeSum == 0:
    print("-1")
else:
    print(primeSum)
    print(min)