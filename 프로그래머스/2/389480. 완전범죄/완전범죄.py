# 1. a: 내림차순으로 정렬
# 2. a가 같다면, b는 오름차순
def solution(info, n, m):
    sort_info = sorted(info, key= lambda x: (-(x[0]-x[1])))
    print(sort_info)
    
    a_cnt = n
    b_cnt = m
    a_recur = 0
    for a_info, b_info in sort_info:
        if b_cnt > b_info:
            b_cnt -= b_info
        else:
            if a_cnt > a_info:
                a_cnt -= a_info
                a_recur += a_info
            else:
                return -1
    return a_recur