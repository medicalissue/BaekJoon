import sys

def input():
    return sys.stdin.readline()[:-1]

N = int(int(input()))
gomCount = 0
chatList = set()

for i in range(N):
    nowChat = input()
    if nowChat == "ENTER":
        gomCount += len(chatList)
        chatList.clear()
    else:
        chatList.add(nowChat)

gomCount += len(chatList)
print(gomCount)