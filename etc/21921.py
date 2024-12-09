import sys
input = sys.stdin.readline
n, x = map(int, input().split())
member = list(map(int , input().split()))

cnt = 1
if sum(member) == 0:
    print("SAD")
else:
    max_anw = sum(member[0:x])
    temp = max_anw
    for i in range(x, n):
        temp += member[i]
        temp -= member[i-x]
        # 다음거가 더 크다면
        if temp > max_anw:
            max_anw = temp
            cnt =1
        elif temp == max_anw:
            cnt +=1
    print(max_anw)
    print(cnt)







# max_idx = x
# cnt = 1
# for i in range(n-x):
#     temp = member[i]
#     # print("temp :", temp)
#     # print("member :", member[i+x])
#     if temp < member[i+x]:
#         max_idx = i+x
#         cnt = 1
#     elif temp == member[i+x]:
#         max_idx = i+x
#         cnt +=1
#     # print("max_idx", max_idx)
#     # print("cnt : ", cnt)

# max_anw = sum(member[max_idx-x+1:max_idx+1])

# if (max_anw == 0):
#     print("SAD")
# else:
#     print(max_anw)
#     print(cnt)
