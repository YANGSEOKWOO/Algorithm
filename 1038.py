import sys
input= sys.stdin.readline

n = int(input())

# dp = [-1]*(1000001)
# k = 9876543210
# num = 0

# for i in range(k):
#     a = ''.join(sorted(set(str(i)),reverse=True))
#     if a == str(i):
#         dp[num] = i
#         num+=1
# print(dp[n])

dp = [-1]*(1000001)
