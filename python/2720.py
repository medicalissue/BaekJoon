coinValue = [25, 10, 5, 1]

howMany = int(input())
returnCoins = [[0 for col in range(4)] for row in range(howMany)]

for i in range(howMany):
    payBack = int(input())
    for j in range(4):
        while payBack - coinValue[j] >= 0:
            payBack -= coinValue[j]
            returnCoins[i][j] += 1

for i in range(howMany):
    print(*returnCoins[i])