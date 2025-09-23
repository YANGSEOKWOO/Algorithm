
# problems의 원소는 [alp_req, cop_req, alp_rwd, cop_rwd, cost]의 형태로 이루어져 있습니다.

# 1.최대 알고력과 최대 코딩력을 구한다.
# 2. cost에 대한 보상 비율을 구한다? 그래서 가장 보상 비율이 높은 걸로 선택? 
# 3. 근데 보상이 알고랑 코딩 둘 다 있는데 어떻게 나눌 수 있을까?? 
# 4. dp 처럼 1,1 ~ max,max 까지 다구하는거는? 

def solution(alp, cop, problems):
    
    max_alp = alp
    max_cop = cop

    ## 최대 알고력과 코딩력 구하기 
    
    for i in range(len(problems)):
        max_alp =max(max_alp, problems[i][0])
        max_cop =max(max_cop, problems[i][1])
    
    
    
    inf = float('inf')
    
    
    problems.sort(key= lambda x: [x[0],x[1]])
    
    dp = [[inf for _ in range(max_cop*2+2)]for _ in range(max_alp*2+2)]

    dp[alp][cop]=0

    answer =max_alp+max_cop-alp-cop+1
    
    for i in range(alp,max_alp+2):
        for j in range(cop,max_cop+2):
            dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
            dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                
                if i>= alp_req and j >=cop_req:    
                    if i+alp_rwd>max_alp and j+cop_rwd>max_cop:
                        dp[max_alp+1][max_cop+1]=min(dp[max_alp+1][max_cop+1],dp[i][j]+cost)
                    elif i+alp_rwd>max_alp:
                        dp[max_alp+1][j+cop_rwd]= min(dp[max_alp+1][j+cop_rwd],dp[i][j]+cost)
                    elif j+cop_rwd>max_cop:
                        dp[i+alp_rwd][max_cop+1]=min(dp[i+alp_rwd][max_cop+1],dp[i][j]+cost)
                    else:
                        dp[i+alp_rwd][j+cop_rwd]=min(dp[i][j]+cost,dp[i+alp_rwd][j+cop_rwd])
                elif i< alp_req and j <cop_req:
                    break
                
    
                

    for i in range(max_alp):
        answer = min(answer, dp[max_alp][max_cop+i])
        answer = min(answer, dp[max_alp+i][max_cop])      
    answer=min(answer,dp[max_alp+1][max_cop+1])

    
    
    return answer
  