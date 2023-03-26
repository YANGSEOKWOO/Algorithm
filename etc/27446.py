n, m = map(int, input().split())
# n : 논문의 마지막 페이지 번호
# m : 바닥에 흩어진 논문의 장수
page = list(map(int, input().split()))

non = [0]*(n+1)
for i in page:
    non[i] = 1
# 1 : 있는논문
# 0 : 잃어버린 논문
# answer = 0
# for i in range(1,n+1):
#     start = False
#     cnt = 0
#     x_cnt = 0
#     if non[i] == 0:
#         if cnt >= 3:  # 따로인쇄
#             if i == n:   # 따로인쇄지만 마지막인 경우
#                 answer += 7
#             else:  # 마지막이 아니라면 그 전까지 한 것 정산
#                 answer += (5 + 2*x_cnt)
#                 x_cnt = 1
#                 cnt = 0
#         else:
#             if i == n:
#                 x_cnt += cnt
#                 answer += (5 + 2*x_cnt)
#                 cnt = 0
#                 x_cnt = 0
#     else:
#         cnt +=1

answer = 0
cnt = 0
x_cnt = 0
for i in range(1,n+1):
    start = False
    
    print(non[i])
    if non[i] == 0:
        if start == False:
            x_cnt +=1
        elif start == True:
            if cnt >= 3:
                answer += (5 + 2*(x_cnt))
                x_cnt = 1
                cnt = 0
                start = False
            elif cnt <2:
                x_cnt += cnt
                answer = (5+2*(x_cnt))
                x_cnt = 1
                cnt = 0
                start = False
    elif non[i] == 1:
        if start == False:
            start = True
            cnt += 1
        else:
            cnt +=1
    print("x_cnt :", x_cnt, end=" ")
    print("cnt : ", cnt, end=" ")
    print("start : ",start)
    print("answer :", answer)
answer += (5+ 2*(x_cnt))
print(answer)

# 잃어버리지 않은 페이지를 인쇄해도 괜찮은 경우
# xox인 경우
# 1. 뿜빠이 5+2, 5+2 => 14
# 2. 다 5 + 2*3 => 11
# xoox인 경우
# 1. 뿜빠이 => 14
# 2. 다 5 + 2*4 => 13
# xooox인 경우
# 1. 뿜빠이 => 14
# 2. 다 5 + 2*5 => 15
# 
# 결론적으로 잃어버린것 사이에 존재하는 페이지가 1개,2개인 경우에
# 잃어버리지 않은 페이지를 인쇄해도 괜찮다.
