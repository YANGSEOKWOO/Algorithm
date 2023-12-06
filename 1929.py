import sys
input = sys.stdin.readline

m, n = map(int, input().split(" "))

graph = [True]*1000001

graph[0] = False
graph[1] = False

for i in range(2, int(n**0.5)+1):
  for j in range(2*i, n+1, i):
    graph[j] = False

for i in range(m, n+1):
  if graph[i]:
    print(i)