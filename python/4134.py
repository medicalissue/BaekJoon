import sys
import math

def input():
    return sys.stdin.readline()[:-1]

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

testCase = int(input())
smallestPrime = [0] * testCase
for i in range(testCase):
    num = int(input())
    while not isPrime(num):
        num += 1
    smallestPrime[i] = num

print(*smallestPrime, sep = "\n")