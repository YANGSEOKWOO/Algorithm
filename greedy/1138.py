# N명 줄세우기
# 마음대로 서지 못하고 
n = int(input())
line = list(map(int, input().split()))
cross_line = [0]*n

len_line = len(line)

for i in range(len_line):
    for j in range(len_line):
        if cross_line[j] != 0:
            continue
        if line[i] == 0:
            cross_line[j] = i + 1
            break
        line[i] -= 1

print(*cross_line)

# 키 모름
'''
아이디어가 중요할 것 같음
1~N까지 키순이네

뒤부터 본다면
키가 제일 크다 => 위치 상관없이 무조건 0
키가 제일 작다 => 위치 고정된다.
1. 큰 사람부터 위치를 찾는게 맞을까
2. 작은 사람부터 위치를 찾는게 맞을까?
=> 큰 사람의 위치는 특정하기 어려움

2번째 사람은 1번째 사람을 어떻게 고려할까?
'''