import sys

def input():
    return sys.stdin.readline()[:-1]

isVPS = list()
T = int(input())

for _ in range(T):
    checkVPS = list(input())
    delFlag = False
    if len(checkVPS) % 2 == 1:
        isVPS.append("NO")
        continue
    for _ in range(int(len(checkVPS) / 2)):
        for i in range(len(checkVPS) - 1):
            if checkVPS[i] == "(" and checkVPS[i + 1] == ")":
                checkVPS[i] = "*"
                checkVPS[i + 1] = "*"
                delFlag = True
        if delFlag:
            while "*" in set(checkVPS):
                checkVPS.remove("*")
        if not checkVPS:
            isVPS.append("YES")
            break
    if checkVPS:
        isVPS.append("NO")

print(*isVPS, sep = "\n")