# A : 예상, B : 실제
# 불만도 |A-B|

# 불만도의 총 합을 최소로 하면서, 학생들의 등수 매기기는?
# 사고과정, 접근법 기록

# 어떻게 해야 불만도가 최소가 될까?
'''
1. 동석차가 없이 등수를 매겨야 한다.
2. 본인의 예상 등수는 중복이 된다.

단순한 생각
- 등수가 맞는게 best이기 때문에, 예상 등수를 dict으로 만든다. ex) {'1':2, '2':1, '3':1, '5':1}
- 등수가 안맞는다면, 최대한 그 등수와 비슷하게 배정을 하는게 좋다고 생각

애매한 부분
- 위 처럼, 등수에 맞게 준다고 쳐본다면
- {'1':2, '2':1, '3':1, '4':1} 의 경우, 1을 예상한 학생은 나머지 자리가 차있기에 5에 들어가게 되는데
- 1) 1을 예상한 학생을 가장 가까운 '2'에 주고 나머지 학생들을 미는 것이 이득인지 (4)
- 2) 1을 예상한 학생을 가장 가까운 '2'에 주고 '2'를 빈 자리에 집어 넣는게 이득인지 (4)
- 3) 그냥 나머지 자리에 1을 예상한 학생을 배정하는 것이 이득인지 (4)
일단 위의 예시에서는 3경우 다 동일한 불만도를 가짐

예제 1
{'1':2, '2':1, '3':1, '4':0, '5':1}
1) 3, 2) 3, 3) 3 동일

애매한 부분
1처럼 꼭짓점에 있는 부분이 아닌, '2'에 여러명이 중복된다면 어떻게 분배해야 하는지
{'1': 0, '2': 1 , '3': 3 , '4': 0 , '5': 1}이라면

그냥 결국, 제 자리를 찾은 애들은 그대로 두고 나머지만 계산하면 최적같은데...

{1:0, 2:2, 3:2, 4:0, 5:0, 6:0}
비어있는 애들 따로 빼서 오름차순으로 만들고
여분있는 애들 따로 빼서 오름차순으로 만들면 될듯

dic: {'3':0, '500000':1}
'''

import math
import sys
input = sys.stdin.readline
n = int(input())
dic = {i:0 for i in range(1,500001)}
extra = dict()
poor = []
for i in range(n):
    num = int(input())
    dic[num] += 1
# for key, value in dic.items():
#     if value >= 2:
#         extra[key] = value
#     elif key > n:
        
#     elif value == 0 and key<=n:
#         poor.append(key)
# sorted_extra = sorted(extra.items())
# print(sorted_extra)
# poor.sort()
# print(poor)
# anw = 0
# cnt = 0
# for key, value in sorted_extra:
#     print(f'key:{key} value:{value}')
#     for i in range(value-1):
#         print(f'poor[cnt]: {poor[cnt]}')
#         anw += abs(key-poor[cnt])
#         cnt += 1

# print(anw)
for key in list(dic.keys()):
    if dic[key] == 0:
        del dic[key]
sorted_extra = sorted(dic.items())
# print(sorted_extra)
poor = [i for i in range(1, n+1)]
# print(poor)
anw = 0
cnt = 0
for key, value in sorted_extra:
    # print(f'key:{key} value:{value}')
    for i in range(value):
        # print(f'poor[cnt]: {poor[cnt]}')
        anw += abs(key-poor[cnt])
        cnt += 1

print(anw)



