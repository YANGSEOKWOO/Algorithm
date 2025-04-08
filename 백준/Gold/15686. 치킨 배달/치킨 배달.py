# arr = [1, 2, 3, 4]
# visited = [0]* len(arr)

# def combinations(n, new_arr, c):
#     if len(new_arr) == n:
#         print(new_arr)
#         return
#     for i in range(c, len(arr)):
#         combinations(n, new_arr + [arr[i]], i+1)
# combinations(2, [], 0)
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

chicken_road = []
home_road = []

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            home_road.append((x,y))
        elif graph[x][y] == 2:
            chicken_road.append((x,y))

anw = []
def calculateRoad(chicken_house):
    total_distance = 0
    for hx, hy in home_road:
        min_distance = float('inf')
        for cx, cy in chicken_house:
            dist = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, dist)
        total_distance += min_distance
    return total_distance

def backtracking(depth, start, chicken_house):
    global m
    global chicken_road
    if depth == m:
        anw.append(calculateRoad(chicken_house))
        return
    # why? => 배열에서 순차적으로 선택해야하니까
    for i in range(start, len(chicken_road)):
        chicken_house.append(chicken_road[i])
        backtracking(depth+1, i+1, chicken_house)
        chicken_house.pop()



backtracking(0,0,[])
print(min(anw))