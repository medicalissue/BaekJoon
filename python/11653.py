n = int(input())

i = 2

while n != 1:
    while True:
        if n % i == 0:
            print(i)
            n = n / i
        else:
            break
    i += 1