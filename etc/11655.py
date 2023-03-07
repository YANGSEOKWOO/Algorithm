word = input()
anw = ''
for i in word:
    if 'a' <= i <= 'z':
        i = ord(i) + 13
        if i > 122:
            i -= 26
        anw += chr(i)
    elif 'A' <= i <= 'Z':
        i = ord(i) + 13
        if i > 90:
            i -= 26
        anw += chr(i)
    else:
        anw += i
print(anw)