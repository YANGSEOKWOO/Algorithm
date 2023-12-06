# 가장 앞의 중요도 확인
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
# 인쇄안하고 Queue의 가장 뒤 재배치

# 기존 문제점 : 1111이런식으로 동일한 숫자의 순번을 어떻게 지정할 것인가?
# index를 지정하는 list를 따로 더 만들어야 하는가?
# 해결 : 본인의 위치만 기록을 해놓으면 되는거임, 빠졌을 때 m -= 1, 
# 그리고나서 내가 뒤로 간 경우는 다시 초기화해주면 되는 거
def queue(printer, num):
  cnt = 0
  while True:
    best = max(printer)
    first = printer.pop(0)
    num -= 1
    
    if best  == first:
      cnt +=1
      if num < 0:
        break
    else:
      printer.append(first)
      if num < 0:
        num = len(printer)-1
  return cnt

import sys
input =sys.stdin.readline
t = int(input())
for _ in range(t):
  n, m = map(int, input().split(" "))
  printer = list(map(int, input().split(" ")))
  anw = queue(printer, m)
  print(anw)
# 두 번째 줄 : N개 문서의 중요도가 차례대로 주어짐

# 맨 왼쪽부터 읽는다.

    