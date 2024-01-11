import math

small, large = list(map(int, input().split()))
maxJegop = int(math.sqrt(large))
cnt = 0

for i in range(small, large + 1):
    isJegopNoNo = True
    for j in range(2, maxJegop + 1):
        if i % math.pow(j, 2) == 0:
            isJegopNoNo = False
            break
    if isJegopNoNo:
        cnt += 1

print(cnt)