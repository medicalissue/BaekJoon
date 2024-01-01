n = int(input())
howMuch = 0

for i in range(1, n - 1):
    howMuch += int((i * (i + 1)) / 2)

print(howMuch)
print("3")