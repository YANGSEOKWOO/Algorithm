from collections import Counter

# 입력 받기
word1 = input().strip()
word2 = input().strip()

# 각 단어의 문자 빈도 계산
count1 = Counter(word1)
count2 = Counter(word2)

# 두 단어의 문자 차이를 계산
difference = (count1 - count2) + (count2 - count1)

# 차이의 총합 계산 (제거해야 할 문자 개수)
result = sum(difference.values())
print(result)