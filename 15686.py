# 칸 : 빈칸, 치킨집, 집

# 치킨 거리 : 집과 가장 가까운 치킨집 사이 거리
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for i in range(n)]
print(city)
