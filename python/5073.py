length = [0] * 3
ans = list()

while True:
    zeroCheck = input()
    if zeroCheck == "0 0 0":
        break

    length = list(map(int, zeroCheck.split()))
    hit = 0
    
    if sum(length) - max(length) <= max(length):
        ans.append("Invalid")
        continue

    for i in range(3):
        if length[i] == length[(i + 1) % 3]:
            hit += 1

    if hit == 3:
        ans.append("Equilateral")
    elif hit == 1:
        ans.append("Isosceles")
    else:
        ans.append("Scalene")

print(*ans, sep = "\n")