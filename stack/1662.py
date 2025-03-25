# s = input()
# stack = []

# for i in s:
#     stack.append(i)


# flag = False
# temp_len =0

# for i in range(len(s)):
#     item = stack.pop()
#     if item == ")":
#         continue
#     # 문자열이라면
#     if item != "(":
#         if flag:
#             temp_len = int(item)*temp_len
#             flag = False
#         else:
#             temp_len += 1
#     if item == "(":
#         flag = True
    
# print(temp_len)


s = input().rstrip()

stack = []          # (이전까지 누적된 길이, 반복 횟수)
curr_len = 0
i = 0

while i < len(s):
    if s[i].isdigit():
        # 다음 문자가 '(' 이면 “K(Q)” 패턴
        if i+1 < len(s) and s[i+1] == '(':
            repeat = int(s[i])
            stack.append((curr_len, repeat))
            curr_len = 0
            i += 2      # 숫자와 '(' 건너뛰기
        else:
            curr_len += 1
            i += 1
    elif s[i] == ')':
        prev_len, repeat = stack.pop()
        curr_len = prev_len + curr_len * repeat
        i += 1
    else:
        # '(' (항상 앞에 숫자가 있으므로 이미 처리됨)
        i += 1

print(curr_len)