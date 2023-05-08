# import math
# n = int(input())
# box = [[0,0]]

# rect = [0,0] 
# # 1번째 : 전체길이
# # 2번째 : 높이

# def check(a,b):
#     # print("rect[0] : ", rect[0], "rect[1] : ", rect[1])
#     # 2번째 값이 세로로 하는게 더 큰 경우다. -> 2번째 값이 세로로 변함!!
#     if abs(rect[1]-b) >= abs(rect[1]-a):
#         rect[0] = rect[0] - rect[1]+a+b+abs(rect[1]-b)
#         rect[1] = b
#     else:
#         rect[0] = rect[0] - rect[1]+a+b+abs(rect[1]-a)
#         rect[1] = a
        
# for i in range(n):
#     box.append(list(map(int, input().split())))

# rect[0] = box[1][0] +box[1][1]
# if 2*box[0][0] <= box[1][0] + box[1][1]:
#     rect[1] = box[1][0]
# else:
#     rect[1] = box[1][1]

# for i in range(2,n+1):
#     check(box[i][0], box[i][1])
# # print(box)
# print(rect[0]-rect[1])
import math

n = int(input())
dp = [[0,0] for i in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
for i in range(1,n): 
    dp[i][0] = max(dp[i-1][0] + abs(arr[i-1][1]- arr[i][1]),dp[i-1][1] + abs(arr[i-1][0]- arr[i][1]) )+ arr[i][0]
    dp[i][1] = max(dp[i-1][0] + abs(arr[i-1][1]- arr[i][0]),dp[i-1][1] + abs(arr[i-1][0]- arr[i][0]) )+ arr[i][1]
print(max(dp[n-1][0], dp[n-1][1]))