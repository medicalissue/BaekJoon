target = 0
line = 0

for i in range(9):
    newNumber = int(input())
    if newNumber > target:
        target = newNumber
        line = i + 1

print(target)
print(line)