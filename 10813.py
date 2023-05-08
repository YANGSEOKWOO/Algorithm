n, m = map(int, input().split())
num = [i for i in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  temp = num[a]
  num[a] = num[b]
  num[b] = temp

for i in range(1, n+1):
  print(num[i], end=" ")
  