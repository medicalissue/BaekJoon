N, K = list(map(int, input().split()))

cnt = 0
printZero = True

for i in range(N):
    if N % (i + 1) == 0:
        cnt += 1
    if cnt == K:
        print(i + 1)
        printZero = False
        break

if printZero:
    print("0")