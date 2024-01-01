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

ansList = list()

while True:
    n = int(input())
    if n == 0:
        break
    to2nPrimeList = eraTos(2 * n)
    hit = 0
    for i in range(n + 1, 2 * n + 1):
        if to2nPrimeList[i] == True:
            hit += 1
    ansList.append(hit)

print(*ansList, sep = "\n")