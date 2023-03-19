import sys
sys.setrecursionlimit(100000)
def find(k):
	if(p[k] == k):
		return k
	p[k] = find(p[k])
	return p[k]

def check(a, b):
    a = find(a)
    b = find(b)
    if (a==b):
        print("YES")
        return
    print("No")
    return

def merge(a, b):
    a = find(a)
    b = find(b)
    if (a==b):
        return
    p[b] = a

n, m = map(int, input().split())
p = [0] * (n+1) # 부모 테이블 생성
for i in range(n+1): # 자기 자신을 부모로 설정
    p[i] = i
# p = []
# for i in range(n+1):
#     p.append(-i)

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        merge(b,c)
    elif a == 1:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")