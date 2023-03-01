n, m = map(int, input().split())
bsk = [0 for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    for i in range(a,b+1):
        bsk[i] = c
for i in range(1,n+1):
    print(bsk[i], end= ' ')