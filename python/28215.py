from itertools import combinations

N, K = list(map(int, input().split()))
houseMap = [[0, 0] for _ in range(N)]
for i in range(N):
    houseMap[i] = list(map(int, input().split()))
possibleWays = list(combinations(houseMap, K))
longestbutshort = 0

for shelter in possibleWays:
    longest = 0
    for nowCheck in houseMap:
        length = [0 for _ in range(K)]
        for i in range(K):
            length[i] = abs(nowCheck[0] - shelter[i][0]) + abs(nowCheck[1] - shelter[i][1])
        if longest == 0:
            longest = min(length)
        else:
            longest = max(longest, min(length))
    if longestbutshort == 0:
        longestbutshort = longest
    else:
        longestbutshort = min(longestbutshort, longest)

print(longestbutshort)