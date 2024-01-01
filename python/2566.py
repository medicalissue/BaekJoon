arr = [[0 for col in range(9)] for row in range(9)]
highScore = [-1] * 3

for i in range(9):
    arr[i] = list(map(int, input().split()))

for i in range(9):
    for j in range(9):
        if highScore[0] < arr[i][j]:
            highScore[0] = arr[i][j]
            highScore[1] = i + 1
            highScore[2] = j + 1

print(highScore[0])
print(highScore[1], highScore[2])