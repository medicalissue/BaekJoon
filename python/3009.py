coord = [[0 for col in range(2)] for row in range(3)]

targetX = 0
targetY = 0

for i in range(3):
    coord[i] = list(map(int, input().split()))

for i in range(3):
    if coord [i][0] == coord[(i + 1) % 3][0]:
        targetX = coord[(i + 2) % 3][0]
    if coord [i][1] == coord[(i + 1) % 3][1]:
        targetY = coord[(i + 2) % 3][1]

print(targetX, targetY)