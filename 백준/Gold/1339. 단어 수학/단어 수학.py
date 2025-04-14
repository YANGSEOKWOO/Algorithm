n = int(input())

num_list = [input() for _ in range(n)]

# print(num_list)
alphabet_dict = dict()

for i in range(n):
    len_str = len(num_list[i])

    for j in range(len_str):
        if num_list[i][j] not in alphabet_dict:
            if j == len_str-1:
                alphabet_dict[num_list[i][j]] = 1
            else:
                alphabet_dict[num_list[i][j]] = 10**(len_str-j-1)
        else:
            if j == len_str-1:
                alphabet_dict[num_list[i][j]] += 1    
            else:
                alphabet_dict[num_list[i][j]] += 10**(len_str-j-1)
# dic = alphabet_dict.sort(key= lambda x: x[1])
check = []
for i, j in alphabet_dict.items():
    # print(f'i:{i} j:{j}')
    check.append((i,j))
# print(alphabet_dict)

check.sort(key=lambda x: -x[1])
# print(check)

cnt = 9
anw = 0
for i, j in check:
    anw += j*cnt
    cnt -=1
print(anw)
