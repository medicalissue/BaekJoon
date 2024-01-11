def isPalindrome(string):
    string = list(string)
    if len(string) % 2 == 1:
        string.pop(int((len(string) - 1) / 2))

    for i in range(int(len(string) / 2)):
        if string[i] == string[-i - 1]:
            continue
            # print(string[i], string[-i -1])
        else:
            return False
    return True


check = input()
flag = False

if len(set(check)) == 1:
    print("-1")
elif isPalindrome(check):
    print(len(check) - 1)
else:
    print(len(check))