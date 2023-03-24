n, m = map(int, input().split())
paper = list(map(int, input().split()))
anw = [0]*(n+1)

for i in paper:
    anw[i] = 1

# print(anw)
if anw[1] == 0:
    last = True
else:
    last = False
answer = []
cnt  = 0 
x_cnt = 0
check = False

for i in range(1,n+1):
    if anw[i] == 0:
        if check == False:
            check = True
            x_cnt = 1
        elif check == True:
            if cnt <=2:
                x_cnt += cnt
                cnt = 0
            x_cnt += 1
        last = False
    elif anw[i] == 1:
        if check ==False:
            continue
        elif check == True:
            cnt += 1
        last = True
    if cnt >= 3:
        answer.append(x_cnt)
        x_cnt =0
        cnt = 0
        check = False
    # print("i : ", i, "anw[i] :", anw[i])
    # print("cnt : ", cnt, " x_cnt : ", x_cnt)
    # print("check :", check, "last : ", last)
    # print("anw :", answer)
    # print()
if last:
    answer.append(x_cnt)
else:
    answer.append(x_cnt+cnt)
# print("last anw :", answer)
result = 0
for i in answer:
    if i == 0:
        break
    result += (5+(2*i))
print(result)
