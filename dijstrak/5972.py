import sys, heapq
input = sys.stdin.readline

n, m = map(int,input().split())
INF = float("inf") # 무한대 상수 선언
graph = [[] for _ in range(n+1)] # 노드와 노드 사이의 거리를 담을 graph 리스트 선언
distance = [INF] * (n+1) # 처음에는 각 지점의 거리를 무한대로 distance 노드의 갯수만큼 초기화
for i in range(m): # 간선의 갯수만큼 
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c)) # 노드 위치와 비용순으로 graph에 집어넣습니다.

def dijkstra(s):
    q = [] 
    distance[s] = 0 # 자기자신과의 거리는 0으로 초기화합니다.
    heapq.heappush(q,(0,s)) # q에 (거리, 위치)를 담습니다.
    while q: 
        dist, cur = heapq.heappop(q) 
        if distance[cur] < dist: # 이미 계산돼 있는 최솟값보다 크다면 확인할 필요도 없으니 다음 반복으로 넘어갑니다.
            continue 
        for next in graph[cur]: # 이웃돼 있는 노드를 확인합니다.
            cost = dist + next[1] # dist 출발 지점에서 현재 노드까지의 거리 + 현재 노드에서 다음 노드까지의 거리
            if cost < distance[next[0]]: # 이미 계산돼 있는 최솟값이 더 작았다면 갱신해줍니다.
                distance[next[0]] = cost 
                heapq.heappush(q,(cost, next[0])) # 새로운 최솟값을 q에 넣고 다음 반복을 진행해줍니다.
    return distance[n]

print(dijkstra(1))