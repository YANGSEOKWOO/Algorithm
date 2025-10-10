## 동점말고 
## 무조건 어피치 점수보다 한개 큰거 또는 0발로 맞춰야함
## 그걸 통해서 비교인데
## 이걸 어떻게 최적화 하는게 좋을까?

## 1. 일단 맨앞이 0이면 무조건 1 
## 2. 

## 그다음부터 계속해서 비교인데 

## DFS?


def solution(n, info):
    answer = []
    max_value= 0 

    def DFS(values,start,cnt):
        nonlocal answer,max_value
        
        if cnt ==0 :
            tmp=0
            for i in range(11):    
                if values[i] > info[i]:
                    tmp+=(10-i)
                else:
                    if info[i]!=0:
                        tmp-=(10-i)
                    
            if max_value < tmp:
                answer=values.copy()
                max_value = tmp 
            elif max_value == tmp :
                if tmp == 0:
                    return 
                for i in range(11):
                    if values[10-i] > answer[10-i] :
                        answer=values.copy()
                        return
                    elif answer[10-i] > values[10-i]:
                        return 
       
            
        
        else:            
            for i in range(start,11):
                if i == 10:
                    values[i]=cnt
                    DFS(values,i+1,0)
                    values[i]=0
                elif cnt >= info[i]+1:
                    values[i]=info[i]+1
                    DFS(values,i+1,cnt-(info[i]+1))
                    values[i]=0

                    
    lion = [0 for _ in range(11)]
    DFS(lion, 0,n)
    if max_value == 0:
        answer =[-1]
            
    return answer