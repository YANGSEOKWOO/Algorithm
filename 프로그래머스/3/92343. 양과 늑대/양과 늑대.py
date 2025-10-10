## 왔다가 갔다가 할 수 있다....
## 그러면 내가 갈 수 있는 곳만 따져서 하면될거같은디


def solution(info, edges):
    res = 0
    tree =[[] for _ in range(20)]
    
    
    ## 부모:[자식]
    for edge in edges:
        parent,child = edge
        tree[parent].append(child)
    
    
    
    ## DFS로 풀어야하나 

    routes=[]
    for child in tree[0]:
        routes.append([info[child],child])
    
    routes.sort()
    
    
    ## 계획
    ## 1.  일단 양을 먼저 먹도록 한다.
    ## 2. 양이 아닐경우 DFS 처럼 행동 

     
    def DFS(routes,sheeps,wolfs):
        nonlocal res
        res=max(res,sheeps)
        if sheeps <= wolfs:
            res=max(res,sheeps)
            return 
        
        if len(routes)  ==0:
            return 
        
        
        for i in range(len(routes)-1,-1,-1):
            animal, node = routes[i]
            tmp=routes[:]
            for child in tree[node]:
                tmp.append([info[child],child])
            tmp.pop(i)
            if animal == 0:
                DFS(tmp,sheeps+1,wolfs)
                
            else:
                DFS(tmp,sheeps,wolfs+1)

        
    
    DFS(routes,1,0)
    
    
    
    
    
    
    
        
    
    return res