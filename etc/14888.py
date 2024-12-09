import sys
input =sys.stdin.readline

n = int(input())
arr= list(map(int, input().split()))
plus, minus, multiple, div = map(int, input().split())

# 시간
# max(n) = 12
# n-1:연산자 개수 :11

# 의문점
# 곱셈을 다 먼저 써버리면 뒤에 더 큰 값이 나온다면 안되지 않나?
# dfs를 쓴다면 순환해야할텐데, +-*/를 경우의 수 만큼 돌아야 하는 상황
# 그 전에는 123 124 234 이렇게 순환을 하는데
# 여기같은 경우 +에 몇번 등장해야하는 지 결정해줘야 함
  
# 순서를 바꾸면 안됌
min_anw = 1e9
max_anw = -1e9


def dfs(i,data):
  global min_anw,max_anw, plus, minus, multiple, div
  if i == n:
    max_anw = max(max_anw, data)
    min_anw = min(min_anw, data)
    return
  if plus>0:
    plus -= 1
    dfs(i+1, data+arr[i])
    plus += 1
  if minus >0:
    minus -=1
    dfs(i+1, data-arr[i])
    minus += 1
  if multiple > 0:
    multiple -=1
    dfs(i+1, data*arr[i])
    multiple +=1
  if div > 0:
    div -=1
    dfs(i+1, int(data/arr[i]))
    div +=1
dfs(1, arr[0])
print(int(max_anw))
print(int(min_anw))
  


# dfs의 인자에 도대체 어떤걸 들어가야 표준화가 될까?
# 내생각, 백트래킹에는 종료조건이 들어가야한다. (마지막에 다 더해준다거나)
# 시작인자로 i값을 통해 유사 for문 처럼 만들 수 있다. arr[i]의 배열에 접근할 수 있다거나


# 그 전까지는 plus, minus 등 연산자가 들어가는 순서를 어떻게 결정할 지 몰랐다.
# 사실 순서는 필요 없었음, => for문을 굳이 돌 필요가 없었다.

