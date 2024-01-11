from collections import deque
import copy

M, N = list(map(int, input().split()))
tomatobox = [[0 for _ in range(M)] for _ in range(N)]
togo = deque()
nextlevel = deque()

for i in range(N):
    tomatobox[i] = list(map(int, input().split()))

for y in range(N):
    for x in range(M):
        if tomatobox[y][x] == 1:
            togo.append([x, y])

cnt = -1

while togo:
    x, y = togo.popleft()
    if x > 0 and tomatobox[y][x - 1] == 0:
        nextlevel.append([x - 1, y])
        tomatobox[y][x - 1] = 1
    if x < M - 1 and tomatobox[y][x + 1] == 0:
        nextlevel.append([x + 1, y])
        tomatobox[y][x + 1] = 1
    if y > 0 and tomatobox[y - 1][x] == 0:
        nextlevel.append([x, y - 1])
        tomatobox[y - 1][x] = 1
    if y < N - 1 and tomatobox[y + 1][x] == 0:
        nextlevel.append([x, y + 1])
        tomatobox[y + 1][x] = 1
    if not togo:
        cnt += 1
        togo = copy.deepcopy(nextlevel)
        nextlevel = deque()

flag = True
for i in range(N):
    if 0 in tomatobox[i]:
        flag = False

if flag:
    print(cnt)
else:
    print("-1")
