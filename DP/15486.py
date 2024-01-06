import sys
input = sys.stdin.readline

# n day
# T : 상담을 완료하는 데 걸리는 기간
# P : 상담을 했을 때 받을 수 있는 금액

n = int(input())
consultings =[[0,0]]
# consultings = [list(map(int, input().split())) for _ in range(n)]
for _ in range(n):
  consultings.append(list(map(int, input().split(" "))))

dp = [0]*(n+1)
for i in range(1, n+1):
  dp[i] = max(dp[i], dp[i-1])
  finish = consultings[i][0] + i -1
  if finish <= n:
    dp[finish] = max(dp[finish], dp[i-1]+consultings[i][1])
  
print(max(dp))
    











# for i in range(n):
#   consultings[i].append(i+consultings[i][0])
# # print(consultings)
# dp = [0]*(n+1)


# print('consultings', consultings)
# for i in range(1,n+1):
#   k = n-i
#   flag = False
#     # ex) 3일이라면, 종료가 3일내에 이뤄지는지
#   if consultings[i-1][2] == i:
#     dp[i] = max(dp[i-consultings[i-1][0]]+consultings[i-1][1], dp[i-1], dp[i])
#     print('i = ',i,'dp= ',dp)
#     flag = True
#     # 일수가 비어있을 때는 어떻게 할 지
#   if flag == False:
#     dp[i] = dp[i-1]
# print(dp)
# print(max(dp)) 