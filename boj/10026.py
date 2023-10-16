import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = []
visited = [[0] * (N) for _ in range(N)]

sum = 0
sum2 = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    graph.append(list(input()))

def dfs(x, y , color):
    visited[x][y] = 1

    for i in range(4):
        x2 = x+dx[i]
        y2 = y+dy[i]
        if 0 <= x2 <= N-1 and 0 <= y2 <= N-1 and visited[x2][y2] == 0:
            if graph[x2][y2] == color:
                visited[x2][y2] = 1
                dfs(x2, y2, color)

for color in ["R","G","B"]:
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0 and graph[x][y] == color:
                dfs(x, y, color)
                sum += 1

for x in range(N):
    for y in range(N):
        if graph[x][y] == "G":
            graph[x][y] = "R"

visited = [[0] * (N) for _ in range(N)]

for color in ["R","B"]:
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0 and graph[x][y] == color:
                dfs(x, y, color)
                sum2 += 1
print(sum, sum2)