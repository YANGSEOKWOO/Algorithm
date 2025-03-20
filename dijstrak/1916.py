import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (비용, 도시)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

dijkstra(start)
print(distance[end])