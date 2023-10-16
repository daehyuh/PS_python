import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
graph = []

sum = 0
sum2 = 0

visited = [[0] * (N) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    graph.append(list(input()))


def dfs(x, y, color):
    visited[x][y] = 1

    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if 0 <= x2 <= N - 1 and 0 <= y2 <= N - 1 and visited[x2][y2] == 0:
            if graph[x2][y2] == color:
                dfs(x2, y2, color)


for color in ['R', 'G', 'B']:
    for i in range(N):
        for j in range(N):
            if graph[i][j] == color and visited[i][j] == 0:
                dfs(i, j, color)
                sum += 1

visited = [[0] * (N) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"

for color in ['R', 'B']:
    for i in range(N):
        for j in range(N):
            if graph[i][j] == color and visited[i][j] == 0:
                dfs(i, j, color)
                sum2 += 1

print(sum, sum2)
