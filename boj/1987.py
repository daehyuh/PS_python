n, m = map(int, input().split())
arr = []
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

ans = 0
alphas = set()

for i in range(n):
    arr.append(list(input()))


def bfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        xx = x + mx[i]
        yy = y + my[i]
        if -1 < xx < n and -1 < yy < n and not arr[xx][yy] in alphas:
            alphas.add(arr[xx][yy])
            bfs(xx, yy, cnt + 1)
            alphas.remove(arr[xx][yy])

alphas.add(arr[0][0])
bfs(0, 0, 1)
print(ans)