import sys
import re

def input():
    return sys.stdin.readline().rstrip()

N, M = list(map(int, input().split()))
wordDict = dict()
for _ in range(N):
    word = input()
    if len(word) >= M:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
lengthSort = sorted(wordDict.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(lengthSort)):
    print(lengthSort[i][0])