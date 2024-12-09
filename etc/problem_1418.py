import math

def prime_number(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i ==0:
            return False
    return True
def real_number(num):
    check_list = []
    for i in range(1,int(math.sqrt(num)+1)):
        print("dk ", i)
        if i == 1:
            check_list.append(1)
        elif num%i ==0 and prime_number(i):
            check_list.append(i)
    return check_list

n = int(input())
k = int(input())
count = 0
for i in range(1,n+1):
    anw_list = real_number(i)
    print(anw_list)
    if anw_list[-1] <= k:
        count +=1
print(count)



# 인수들을 list에 소수판별 후 넣기