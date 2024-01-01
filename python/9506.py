while True:
    divSum = 0
    n = int(input())
    perfectStr = str(n) + " = "
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            divSum += i
            perfectStr += str(i) + " + "
    if divSum == n:
        print(perfectStr[0:-3])
    else:
        print(str(n) + " is NOT perfect.")