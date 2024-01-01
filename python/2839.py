N = int(input())
howMuch = -1

for i in range(0, int(N / 5) + 1):
    if (N - (i * 5)) % 3 == 0:
        if howMuch == -1:
            howMuch = i + int((N - (i * 5)) / 3)
        else:
            howMuch = min(howMuch, i + int((N - (i * 5)) / 3))

print(howMuch)