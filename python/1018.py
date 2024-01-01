N, M = list(map(int, input().split()))
chessBoard = [["" for col in range(M)] for row in range(N)]
bBoard = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
wBoard = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
for i in range(N):
    chessBoard[i] = list(input())
minFill = -1

for y in range(N - 7):
    for x in range(M - 7):
        bCount = 0
        wCount = 0
        for checkRow in range(8):
            for checkCol in range(8):
                if chessBoard[y + checkRow][x + checkCol] != bBoard[checkRow][checkCol]:
                    bCount += 1
                if chessBoard[y + checkRow][x + checkCol] != wBoard[checkRow][checkCol]:
                    wCount += 1
        if minFill == -1:
            minFill = min(bCount, wCount)
        else:
            minFill = min(minFill, bCount, wCount)

print(minFill)

                