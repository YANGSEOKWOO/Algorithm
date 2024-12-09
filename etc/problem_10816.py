
import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split(" ")))

dic = dict()
for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if m_list[i] in dic:
        print(dic[m_list[i]], end= " ")
    else:
        print(0, end= " ")

# 웬만한 이분탐색으로는 불가능!
# 왜냐하면 찾는거 + 몇개있는 지를 찾아야 하기 때문임
# 그래서 해시테이블 -> 딕셔너리랑 비슷한 개념
# 알아야 하는 개념
# 리스트 안에서 중복되는 애들이 몇개있는지 세고 나중에 그 값을 찾아야 하는 상황
# dict를 사용해서 찾을 때 시간이 오래걸리지 않고 키값을 통해 찾을 수 있다.