import sys

def input():
    return sys.stdin.readline()[:-1]

stack = list()

N = int(input())

for _ in range(N):
    todo = input()
    if len(todo) > 1:
        num = list(map(int, todo.split()))[1]
        stack.append(num)
        continue
    todo = int(todo)
    if todo == 2:
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif todo == 3:
        print(len(stack))
    elif todo == 4:
        if stack:
            print("0")
        else:
            print("1")
    elif todo == 5:
        if stack:
            print(stack[len(stack) - 1])
        else:
            print("-1")