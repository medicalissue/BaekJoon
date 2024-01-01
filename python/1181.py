import sys
input = sys.stdin.readline

N = int(input())
wordList = list()
for _ in range(N):
    word = input()[:-1]
    wordList.append([len(word), word])
wordList.sort()

for i in range(N):
    if i != 0 and wordList[i][1] == wordList[i - 1][1]:
        continue
    print(wordList[i][1])