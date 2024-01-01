word = list(input())
word.reverse()
rev = list(word)
word.reverse()

if rev == word:
    print("1")
else:
    print("0")