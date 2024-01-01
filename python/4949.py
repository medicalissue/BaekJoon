import sys
from collections import deque

def input():
    return sys.stdin.readline()[:-1]

isBalanced = list()

while True:
    sentence = input()
    if sentence == ".":
        break
    sentence = list(sentence)
    delNum = deque()
    for i in range(len(sentence)):
        if sentence[i] != "(" and sentence[i] != ")" and sentence[i] != "[" and sentence[i] != "]":
            delNum.appendleft(i)
    for i in range(len(delNum)):
        del sentence[delNum[i]]

    if len(sentence) % 2 == 1:
        isBalanced.append("no")
        continue
    for _ in range(int(len(sentence) / 2)):
        for i in range(len(sentence) - 1):
            if sentence[i] == "(" and sentence[i + 1] == ")":
                sentence[i] = "*"
                sentence[i + 1] = "*"
                delFlag = True
            elif sentence[i] == "[" and sentence[i + 1] == "]":
                sentence[i] = "*"
                sentence[i + 1] = "*"
                delFlag = True
        if delFlag:
            while "*" in set(sentence):
                sentence.remove("*")
        if not sentence:
            break
    if sentence:
        isBalanced.append("no")
    else:
        isBalanced.append("yes")

print(*isBalanced, sep = "\n")