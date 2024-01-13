# n번쨰 영화 제목 => n번째로 작은 종말의 수

number = 666
cnt = 0
n = int(input())
# Q. 1씩 증가시키는게 과연 빠를까?
while cnt != n:
    if '666' in str(number):
        cnt +=1
    number +=1

print(number-1)

## 다른 풀이