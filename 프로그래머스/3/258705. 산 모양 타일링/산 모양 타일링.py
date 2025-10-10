def solution(n, tops):
    answer = 0
    dp=[[0,0] for _ in range(n+1)] # x, 왼,오
    
    if tops[0] ==1:
        dp[0]=[3,1] # 오른쪽 안들어간 것 ,오른쪽이 들어간것    
    else: 
        dp[0] = [2,1]
    
    
    for i in range(1,n):
        if tops[i] == 0:
            dp[i][0] = dp[i-1][0]*2+dp[i-1][1] 
            dp[i][1] = dp[i-1][0]+dp[i-1][1]
            dp[i][0]%=10007
            dp[i][1]%=10007
        else:
            dp[i][0] = dp[i-1][0]*3+dp[i-1][1]*2
            dp[i][1] = dp[i-1][0]+dp[i-1][1]
            dp[i][0]%=10007
            dp[i][1]%=10007
        
    
    
    
    answer =(dp[n-1][0]+dp[n-1][1])%10007
    
    
    return answer