import sys
input = sys.stdin.readline

n = int(input())
anw = dict()
for i in range(n):
    num = int(input())
    if num in anw:
        anw[num] += 1
    else:
        anw[num] = 1
print(sorted(anw.items(), key = lambda x:(-x[1],x[0]))[0][0])