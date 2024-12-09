# 해시함수 : 임의의 길이의 입력을 받아서 고정된 길이의 출력을 내보내는 함수
# 비둘기집 원리 때문에, 서로 다른 문자열이라도 동일한 해시 값을 가질 수 있다.

import sys
input =sys.stdin.readline

l = int(input())
word= input()
anw = 0
for i in range(l):
  anw += ((ord(word[i])-96)*(31**i))
print(anw%1234567891)
