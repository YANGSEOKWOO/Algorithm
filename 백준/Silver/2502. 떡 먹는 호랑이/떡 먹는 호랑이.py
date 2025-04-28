'''
오늘 호랑이에게 몇 개의 떡을 줬는지
떡을 준 지 며칠이 되었는지
D: 날짜
K: D날에 준 떡의 개수

'''
d, k = map(int, input().split())

a_dp = [0, 1, 0] + [0]*28
b_dp = [0, 0, 1] + [0]*28

for i in range(3,31):
    a_dp[i] = a_dp[i-1] + a_dp[i-2]
    b_dp[i] = b_dp[i-1] + b_dp[i-2]

flag = False
for i in range(1, k):
    for j in range(i,k+1):
        if a_dp[d]*i + b_dp[d]*j == k:
            print(i)
            print(j)
            exit()
