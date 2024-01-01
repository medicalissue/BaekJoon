numList = [0] * 5
for i in range(5):
    numList[i] = int(input())

print(int(sum(numList) / 5))
print(sorted(numList)[2])