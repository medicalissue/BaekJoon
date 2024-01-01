numList = list(map(int, input().split()))
numList.sort()
numList.reverse()
print(*numList, sep="")