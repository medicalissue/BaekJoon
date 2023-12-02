length = int(input())
numList = list(map(int, input().split()))
v = int(input())
howMany = 0

for i in range(length):
    if numList[i] == v:
        howMany += 1

print(howMany)