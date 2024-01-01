import sys

def input():
    return sys.stdin.readline()[:-1]

howMany = int(input())
yaksuList = list(map(int, input().split()))
yaksuList.sort()

print(yaksuList[0] * yaksuList[howMany - 1])