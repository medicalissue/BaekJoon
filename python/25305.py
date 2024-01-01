N, k = list(map(int, input().split()))
score = list(map(int, input().split()))
print(sorted(score)[N - k])