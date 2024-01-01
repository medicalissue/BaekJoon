N = int(input())
ans = 0

for i in range(1, N):
    listNum = list(map(int, str(i)))
    if N == i + sum(listNum):
        ans = i
        break

print(ans)