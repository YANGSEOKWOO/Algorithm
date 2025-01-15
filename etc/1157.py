import math
string = input()

new_str = string.upper()
alpha_list = [0]*26

for i in new_str:
    alpha_list[int(ord(i))-65] += 1


# 1. 최고인 알파벳을 알아야함 => 그게 곧 위치
# 2. 값도 찾아야 함

max_num = alpha_list[0]
max_word = chr(65)
for i in range(len(alpha_list)):
    if max_num < alpha_list[i]:
        max_num = alpha_list[i]
        max_word = chr(65 + i)

cnt = 0
for i in alpha_list:
    if i == max_num:
        cnt +=1

if cnt == 1:
    print(max_word)
else:
    print('?')
