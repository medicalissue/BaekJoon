import sys
import math

def input():
    return sys.stdin.readline()[:-1]

def eraTos(n):
    primeList = [True] * (n + 1)
    primeList[0] = False
    primeList[1] = False
    for i in range(2, n + 1):
        if primeList[i] == True:
            j = 2
            while i * j <= n:
                primeList[i * j] = False
                j += 1
    return primeList

maxN = 1000001
toMaxNPrimeList = eraTos(maxN)
T = int(input())
ansList = list()

for i in range(T):
    n = int(input())
    hit = 0
    for i in range(2, int(n / 2) + 1):
        if toMaxNPrimeList[i] == True and toMaxNPrimeList[n - i] == True:
            hit += 1
    ansList.append(hit)

print(*ansList, sep = "\n")