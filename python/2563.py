coord = [[False for col in range(100)] for row in range(100)]

paperNum = int(input())
area = 0

for _ in range(paperNum):
    left, down = list(map(int, input().split()))
    for i in range(10):
        for j in range(10):
            coord[left + i][down + j] = True

for i in range(100):
    for j in range(100):
        if coord[i][j]:
            area += 1

print(area)