# 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity
# 출입구 -> 봉우리 -> 출입구 
# intensity 가장 최소가 되는 곳  즉  휴식 노드끼리의 거리가 가장 짧아야함 
# 그렇다면 일단 출발지에서 출발하는데 가장 짧은 거리를 기준으로 가는 걸로 
# 돌아오는것은 그대로 오는것 어차피 이미 최대값이 정해졌고 그것보다 작은값으로 온다고 하더라도 의미가 없기 때문이다. 

## 그래서 시작부터 봉우리까지 계속 작은값으로 가는걸로만 따져서 하면 될거 같다 .


import heapq

def solution(n, paths, gates, summits):
    answer = []
    board = [[] for _ in range(n+1)]
    
    
    for path in paths:
        start, end, w = path
        board[start].append([end,w])
        board[end].append([start,w])
    
    
    
    ch=[0 for _ in range(n+1)]
    for i in range(len(gates)):
        ch[gates[i]] = 1
    
    for i in range(len(summits)):
        ch[summits[i]] = -1
        

    min_summit= 10000001
    intensity = 10000001 
    
    visited= [0 for _ in range(n+1)]
    
    hq = []
    for gate in gates:
        for direction in board[gate]:
            node , weight = direction
            heapq.heappush(hq,(weight, node))
          
    while hq:
        w, node =heapq.heappop(hq)
        if intensity < w:
            continue
        if visited[node]==1:
            continue
        if ch[node] == -1:  
            if min_summit > node:
                min_summit = node
                intensity = w 
        elif ch[node] == 0:
            for direct in board[node]:
                nxt_node, nxt_weight = direct
                if ch[nxt_node] != 1 :
                    visited[node]=1
                    heapq.heappush(hq,(max(w,nxt_weight), nxt_node))
    

    return [min_summit,intensity]

