import sys
input = sys.stdin.readline
inf = 100001
n, k = map(int, input().split())

dp = [inf]*100

for i in range(1, n+2):
    
    dp[i] = min(dp[i-1], dp[i+1], dp[i//2]+1)
# 의문
# dp[n]에서 고려해줘야 하는 것
# n//2에서 점프뛰고 온 것, n-1에서 온 것, n+1에서 온 것
# 이렇게 되어있는데, n+1은 값의 초기화가 되지 않아서
# 미리 해놔야함;

# dp[n] = 1
# for i in range(n+1, k+1):
#     if i >= n*2:
#         if i%2 == 0:
#             dp[i] = min(dp[i-1], dp[i+1], dp[i//2])+1
#         else:
#             dp[i] = min(dp[i-1], dp[i+1])+1
#     else:
#         dp[i] = min(dp[i-1], dp[i+1])+1

        

# print('dp', dp)
# print(dp[k])