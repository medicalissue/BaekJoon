N = int(input())

for i in range(N):
    temp = ""
    for _ in range(N - i - 1):
        temp += " "
    for _ in range(i * 2 + 1):
        temp += "*"
    print(temp)

for i in range(N - 1):
    temp = ""
    for _ in range(i + 1):
        temp += " "
    for _ in range(N * 2 - i * 2 - 3):
        temp += "*"
    print(temp)