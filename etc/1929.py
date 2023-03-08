import sys
input = sys.stdin.readline

m, n = map(int, input().split())
aera = [i for i in range(n+1)]
anw = 0

for i in range(2, int((n**0.5))+1):
    if aera[i]:
        j = 2
        while i * j <= n:
            aera[i*j] = False
            j+=1
for i in range(m, n+1):
    if aera[i]:
        print(i)