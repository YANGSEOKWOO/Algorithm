# 알고있는 사실 광주FC가 치른 총 경기 수 (n)
# 경기에서 득점한 골들의 총 합 (a)
# 경기에서 실점한 골들의 총 합(b)
# 분배해서 무승부인 경기가 최소가 되도록 조작
# 1. 가능한 무승부 횟수의 최소값 출력
# 2. 경기 중 일어날 수 있는 최소 무승부 횟수 계산 + 최소 무승부 횟수가 포함된 경기 점수 목록 출력
2, 4

# 1. 가능한 무승부 횟수의 최소값
# 2. 경기 점수 목록을 라인별로 x:y 형식으로 출력

n = int(input())
a = int(input())
b = int(input())

if n ==1:
    if a == b:
        print(1)
        print(f'{a}:{b}')
    else:
        print(0)
        print(f'{a}:{b}')
else:
    if (a+b>= n):
        x, y = min(a, b), max(a, b)
        start = 0
        print(0)
        if a == x:    
            for i in range(n):
                if i == n-1:
                    print(f'{x}:{y-start}')
                else:
                    if x != 0 and i != n:
                        print(f'{1}:0')
                        x -= 1
                    elif x ==0 and i!=n:
                        print(f'{x}:{1}')
                        start +=1
        else:
            for i in range(n):
                if i == n-1:
                    print(f'{y-start}:{x}')
                else:
                    if x != 0 and i != n:
                        print(f'0:{1}')
                        x -= 1
                    elif x ==0 and i!=n:
                        print(f'1:{x}')
                        start +=1
            
    else:
        k = n-(a+b)
        print(k)
        for _ in range(k):
            print("0:0")
        x, y = min(a, b), max(a, b)
        start = 0
        if a == x:    
            for i in range(a+b):
                if i == a+b-1:
                    print(f'{x}:{y-start}')
                else:
                    if x != 0 and i != a+b:
                        print(f'{1}:0')
                        x -= 1
                    elif x ==0 and i!=a+b:
                        print(f'{x}:{1}')
                        start +=1
        else:
            for i in range(a+b):
                if i == n-1:
                    print(f'{y-start}:{x}')
                else:
                    if x != 0 and i != a+b:
                        print(f'0:{1}')
                        x -= 1
                    elif x ==0 and i!=a+b:
                        print(f'1:{x}')
                        start +=1