a, b = map(int, input().split())
a_card = ''.join(list(map(str, input().split())))
test_card = a_card
b_card = list(map(int, input().split()))
# print(a_card)
start = 0

idx = 0
num = 0
flag = False
anw = []

for i in range(b):
    check = test_card.find(str(b_card[i]))
    # print(check)
    if check != -1 and flag == False: # 처음 찾았을 때
        idx = check
        flag = True
        num = 1
        test_card = test_card[:idx] + test_card[idx+1:]
    elif check == -1 or check < idx:
        # 문자가 없거나, 그 전에있다면
        if check != -1:
            # 다시 초기화
            anw.append(num)
            idx = check
            flag = True
            num = 1
            test_card = test_card[:idx] + test_card[idx+1:]
        else:
            anw.append(num)
            flag = False
            num = 0
            idx = 0
            test_card= a_card
    elif check > idx:
        idx = check
        num +=1
        test_card = test_card[:idx] + test_card[idx+1:]

anw.append(num)
# print(anw)
print(max(anw))