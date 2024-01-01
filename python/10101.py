angles = [0] * 3
hit = 0
angSum = 0

for i in range(3):
    angles[i] = int(input())
    angSum += angles[i]
for i in range(3):
    if angles[i] == angles[(i + 1) % 3]:
        hit += 1

if angSum != 180:
    print("Error")
elif hit == 3:
    print("Equilateral")
elif hit == 1:
    print("Isosceles")
else:
    print("Scalene")