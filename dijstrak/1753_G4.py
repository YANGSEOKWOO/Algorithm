import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
dist = [INF]*(v+1)
heap = []

def dijkstra(start):
    dist[start] = 0
    heapq.heappush(heap, (0 ,start))

    while heap:
        w, now = heapq.heappop(heap)
        if dist[now] < w:
            continue
        for wei, dest in graph[now]:
            cost = dist[now] + wei
            if cost < dist[dest]:
                dist[dest] = cost
                heapq.heappush(heap,(cost, dest))
dijkstra(start)
for i in range(1, v+1):
    print("INF" if dist[i] == INF else dist[i])

# visited = [False]*(v+1)

# for i in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))

# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, v+1):
#         if not visited[i] and dist[i] < min_value:
#             min_value = dist[i]
#             index = i
#     return index

# def dijkstra(start):
#     dist[start] = 0
#     visited[start] = True
#     for i in graph[start]:
#         dist[i[0]] = i[1]
    
#     for i in range(v-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = dist[now] + j[1]
#             if cost < dist[j[0]]:
#                 dist[j[0]] = cost

# dijkstra(start)

# for i in range(1, v+1):
#     if dist[i] == INF:
#         print("INFINITY")
#     else:
#         print(dist[i])