import sys
import heapq
input = sys.stdin.readline


v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]

INF = 1e9
distance = [INF]*(v+1)

for i in range(e):
    u, v, w = map(int ,input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    # 총 비용, 도착노드
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        # i[0]: 도착 노드 번호, i[1]: 간선 가중치
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
# import sys
# input = sys.stdin.readline


# v, e = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(v+1)]

# INF = 1e8

# visited = [False]*(v+1)
# distance = [INF]*(v+1)

# for i in range(e):
#     u, v, w = map(int ,input().split())
#     graph[u].append((v, w))

# def get_smallest_node():
#     min_value = INF
#     index = 0

#     for i in range(1, v+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True

#     for i in graph[start]:
#         distance[i[0]] = i[1]
    
#     for _ in range(v-1):
#         now = get_smallest_node()
#         visited[now] = True

#     for j in graph[now]:
#         if distance[now] + j[1] < distance[j[0]] and not visited[j[0]]:
#             distance[j[0]] = distance[now] + j[1]

# dijkstra(start)
# for i in range(1, len(distance)):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])