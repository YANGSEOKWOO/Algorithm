# 정해진 총액 이하에서 가능한 한 최대의 총 예산
'''
1. 모든 요청이 배정될 수 있다 => 요청한 금액 그대로 배정
2. 모든 요청이 배정될 수 X => 특정한 정수 상한액을 계산하여 
- 상한액 이상인 예산요청 => 모두 상한액을 배정
- 상한액 이하인 예산요청 => 요청한 금액 그대로 배정
'''

# n : 지방의 수
# amount : 예산 양
n = int(input())
request_budget = list(map(int, input().split()))
amount = int(input())

def check(mid, amount):
    global request_budget
    cnt = 0
    for i in request_budget:
        if i > mid:
            cnt += mid
        else:
            cnt +=i
    # 예산보다 적게 책정
    return cnt <= amount
if sum(request_budget) <= amount:
    print(max(request_budget))
else:
    lo = 0
    hi = 1000000000
    while (lo+1) < hi:
        mid = (lo+hi)//2
        if check(mid, amount):
            lo = mid
        else:
            hi = mid
    print(lo)

