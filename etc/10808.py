alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = [0 for i in range(26)]
n = input()

for i in n:
    a[alphabet.find(i)] += 1

for i in a:
    print(i, end=' ')