import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

hear = set()
see = set()

for i in range(n):
    hear.add(input().rstrip('\n'))
for i in range(m):
    see.add(input().rstrip('\n'))

anw = list(hear & see)
print(len(anw))
for i in sorted(anw):
    print(i)
