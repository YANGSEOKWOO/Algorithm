import sys
input = sys.stdin.readline
def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

n = int(input())
hard = [int(input()) for i in range(n)]
hard.sort()
if n == 0:
    print(0)
else:
    top =int(roundTraditional(n*0.15, 0))
    print(int(roundTraditional(sum(hard[top:n-top])/len(hard[top:n-top]), 0)) )


# 파이썬 반올림 함수 round 이슈
# - 우리가 생각하는 반올림 => 사사오입
# - 파이썬이 적용하는 반올림 => 오사오입
# 사사오입 : 4이하의 숫자는 내림, 5이상의 숫자는 올림
# 오사오입 : 5미만의 숫자는 내림, 5초과의 숫자는 올림,
#         5인 경우, 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내린다.
