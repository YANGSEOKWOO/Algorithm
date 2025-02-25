# 팩토리얼 0의 개수

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return list(str(num))

n = int(input())
n_string = factorial(n)
cnt = 0
for i in n_string[::-1]:
    if i == '0':
        cnt +=1
    elif i != '0':
        break
print(cnt)