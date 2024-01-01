a, b, c, d, e, f = list(map(int, input().split()))
ans = list()
brkFlag = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            ans.append(x)
            ans.append(y)
            brkFlag = True
            break
    if brkFlag:
        break

print(*ans)