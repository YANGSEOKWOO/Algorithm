import sys
input = sys.stdin.readline

max_int = sys.maxsize
n = int(input())
m = int(input())

min_cost = [[max_int]*n for _ in range(n)]
for i in range(m):
  a, b, c = map(int, input().split())
  min_cost[a-1][b-1] = min(min_cost[a-1][b-1], c)


for k in range(n):
  for i in range(n):
    for j in range(n):
      if(i == j):
        min_cost[i][j] = 0
      if(i==j or i==k or j == k):
        pass
      min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])

for i in range(n):
  for j in range(n):
    if(min_cost[i][j] == max_int):
      print("0", end=" ")
    else:
      print(min_cost[i][j], end=" ")
  print()