import sys

def input():
    return sys.stdin.readline()[:-1]

moneyStack = list()
K = int(input())

for _ in range(K):
    todo = int(input())
    if todo == 0:
        moneyStack.pop()
    else:
        moneyStack.append(todo)

print(sum(moneyStack))