m, n = map(int, input().split())

eratos = [True for _ in range(n+1)]
eratos[1] = False
end = int(n**(1/2))
for i in range(2, end+1):
    if eratos[i] == False:
        continue
    j = 2
    while i * j <= n:
        eratos[i*j] = False
        j +=1 

for i in range(m, n+1):
    if eratos[i]:
        print(i)
