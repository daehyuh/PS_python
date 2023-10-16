n, m = map(int, input().split(" "))

arr = []

for i in range(0, n+1):
    arr.append([])

for i in range(m):
    a, b, c = map(int, input().split(" "))
    if a == 0:
        arr[b].append(c)
    else:
        if c in arr[b]:
            print("Yes")
        else:
            print("No")