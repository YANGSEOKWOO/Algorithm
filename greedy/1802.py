
# 1 : OUT(시계방향), 0 : IN(반시계방향)

# 어떤 경우에 다시 접을 수 있다는 것을 알 수 있을까?
def can_fold(paper):
    n = len(paper)
    if n == 1:
        return True
    mid = n//2
    for i in range(mid):  # 중앙 기준으로 대칭 확인
        if paper[i] == paper[-i-1]:  # 서로 다른 방향이어야 함
            return False

    front = paper[:mid]
    back = paper[mid+1:]
    return can_fold(front) and can_fold(back)
t = int(input())
for _ in range(t):
    paper = input()
    if can_fold(paper):
        print("YES")
    else:
        print("NO")