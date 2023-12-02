length, target = list(map(int, input().split()))
numList = list(map(int, input().split()))
corrct = ""

for i in range(length):
    if numList[i] < target:
        corrct += str(numList[i]) + " "

corrct == corrct[:-1]
print(corrct)