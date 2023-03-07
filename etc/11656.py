n = input()
anw = []
for i in range(len(n)):
    anw.append(n[i:])
anw.sort()
for i in anw:
    print(i)