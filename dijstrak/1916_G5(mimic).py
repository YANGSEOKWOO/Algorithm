import math
import heapq
input = heapq
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    # u 라는 정점에서 v 정점까지 가는것의 비용을 tuple형태로 만듬
    graph[u].append((v,w))
st, ed = map(int, input().split())

dist = [INF]*(n+1)
# dist : 각 정점의 거리를 담은 list -> 나중에 최소로 바뀜

def dijkstra(start):
    dist[start] = 0
    # 1. 시작점의 거리를 0으로 만든다.
    q = [(0,st )]
    # 

    while q:
        w, cur = heapq.heappop(q)
        # 첫번쨰의 경우 w에 0, cur에 st가 들어간다.
        if dist[cur] < w:
            # 이미 처리 되었다면 무시?
            continue
        
        for dest, wei in graph[cur]:
            cost = dist[cur] + wei
            if dist[dest] > cost:
                dist[dest] = cost
                heapq.heappush(q, (cost, dest))

def dijkstra_2(start):
    dist[start] = 0
    q = [(0, st)]

    while q:
        w, cur = heapq.heappop(q)
        if dist[cur] < w:
            continue
        
        for dest, wei in graph[cur]:
            cost = dist[cur] + wei
            if dist[dest] > cost:
                dist[dest] = cost
                heapq.heappush(q,(cost,dest))


import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
st, ed = map(int, input().split())

dist= [INF]*(n+1)
def dijkstra(start):
    dist[start] = 0
    q = [(start, 0)]

    while q:
        now, cost = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for dest, wei in graph[now]:
            road = dist[now] + wei
            if road < dist[dest]:
                dist[dest] = road
                heapq.heappush(q,(dest,cost))
dijkstra(st)
print(dist[ed])