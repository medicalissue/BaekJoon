N, M = list(map(int, input().split()))

a = [[0 for col in range(M)] for row in range(N)]
b = [[0 for col in range(M)] for row in range(N)]
sum = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    a[i] = list(map(int, input().split()))
        
for i in range(N):
    b[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        sum[i][j] = a[i][j] + b[i][j]

for i in range(N):
    print(*sum[i])