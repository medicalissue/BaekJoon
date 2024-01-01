num, notation = list(map(int, input().split()))
length = 0

while num - notation ** length >= 0:
    length += 1

newNum = [""] * length

for i in range(length):
    tempNum = 0
    while num - notation ** (length - i - 1) >= 0:
        num = num - notation ** (length - i - 1)
        tempNum += 1
    if tempNum < 10:
        newNum[i] = str(tempNum)
    else:
        newNum[i] = str(chr(tempNum + 55))

newNum = "".join(newNum)

print(newNum)