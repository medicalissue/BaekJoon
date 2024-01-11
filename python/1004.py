import math

def isInside(x, y, cometX,cometY, cometR):
    if math.sqrt(pow(x - cometX, 2) + pow(y - cometY, 2)) < cometR:
        return True
    else:
        return False

T = int(input())

for _ in range(T):
    princeX, princeY, destX, destY = list(map(int, input().split()))
    n = int(input())
    cnt = 0
    for _ in range(n):
        eunhaX, eunhaY, eunhaR = list(map(int, input().split()))
        if isInside(princeX, princeY, eunhaX, eunhaY, eunhaR) and isInside(destX, destY, eunhaX, eunhaY, eunhaR):
            continue
        elif isInside(princeX, princeY, eunhaX, eunhaY, eunhaR) or isInside(destX, destY, eunhaX, eunhaY, eunhaR):
            cnt += 1
    print(cnt)