N = int(input())

score = list(map(int, input().split()))
highScore = 0
sum = 0

for i in range(N):
    highScore = max(highScore, score[i])

for i in range(N):
    sum += score[i] / highScore * 100

print(sum / N)