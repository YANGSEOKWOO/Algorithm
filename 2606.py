import sys
input = sys.stdin.readline

# 컴퓨터의 수
n = int(input())
# 연결된 컴퓨터 쌍의 수
v = int(input())
graph = [ i for i in range(n+1)]

# 문제점 : 1하고 나중에 연결되면 끝남
for i in range(v):
    a, b = map(int, input().split(" "))
    if graph[a] > graph[b]:
        temp = b
        b = a
        a = temp
    for j in range(n+1):
        if graph[j] == graph[b] and j!= b:
            graph[j] = graph[a]
    graph[b] = graph[a]

anw = -1
for i in graph:
    if i == 1:
        anw +=1
# print(graph)
print(anw)