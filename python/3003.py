originalChess = [1, 1, 2, 2, 2, 8]
nowChess = list(map(int, input().split()))
howManyPiece = [0] * 6

for i in range(6):
    howManyPiece[i] = originalChess[i] - nowChess[i]

print(*howManyPiece)