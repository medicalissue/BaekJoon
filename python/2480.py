DICE = list(map(int, input().split()))

samenum = 0
cnt = 0
prize = 0
highScore = 0

for i in range(3):
    if DICE[i] == DICE[(i + 1) % 3]:
        samenum = DICE[i]
        cnt += 1
    highScore = max(DICE[i], highScore)

if cnt == 3:
    prize = 10000 + samenum * 1000
elif cnt == 1:
    prize = 1000 + samenum * 100
else:
    prize = highScore * 100

print(prize)