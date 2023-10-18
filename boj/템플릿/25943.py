n = int(input())
left = 0
right = 0
arr = list(map(int, input().split(" ")))
left = arr[0]
right = arr[1]

for i in range(2, n):
    if left == right:
        left += arr[i]
    elif left < right:
        left += arr[i]
    else:
        right += arr[i]
dif = max(left, right) - min(left, right)

masses = [100, 50, 20, 10, 5, 2, 1]
res = 0
for i in masses:
    res += dif//i
    dif %= i

print(res)