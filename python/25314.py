n = int(input())
longNum = int(n / 4)

ans = ""

for i in range(longNum):
    ans += "long "

ans += "int"

print(ans)