num, notation = input().split()
intNum = [0] * len(num)
notation = int(notation)
realNum = 0

for i in range(len(num)):
    try:
        intNum[i] = int(num[i])
    except:
        intNum[i] = ord(num[i]) - 55

intNum.reverse()

for i in range(len(intNum)):
    realNum += (intNum[i]) * (notation ** i)

print(realNum)