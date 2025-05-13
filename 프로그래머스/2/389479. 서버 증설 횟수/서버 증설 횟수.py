# 서버 증설 조건 m
# 서버 운영시간 k

def solution(players, m, k):
    server = []
    # Player식
    # 특정 이용자수가 i 일 때 필요한 서버의 개수를 구하는 식
    # i//m 
    answer = 0
    for i in players:
        server_cnt = len(server)
        print(f'server:{server}, i:{i}, ')
        if i//m > server_cnt:
            for j in range(i//m - server_cnt):
                server.append(k)
                answer +=1
        idx = 0
        while idx < len(server):
            server[idx] -= 1
            if server[idx] == 0:
                server.pop(idx)
            else:
                idx += 1
    print(server)
    return answer