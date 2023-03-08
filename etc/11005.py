alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

num, b = map(int, input().split())
anw = ''
while num!= 0:
    anw += str(alphabet[num % b])
    num = num // b
print(anw[::-1])


# 결론적으로 num 이라는 숫자를 
# b의 제곱 형태로 표현해야 한다. 라는 것!
