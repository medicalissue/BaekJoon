arr = [["*" for col in range(15)] for row in range(5)]
ans = ""

for i in range(5):
    tempWord = input()
    for j in range(len(tempWord)):
        arr[i][j] = tempWord[j]

for i in range(15):
    for j in range(5):
        if arr[j][i] != "*":
            ans += arr[j][i]

print(ans)