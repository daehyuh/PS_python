a = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i%10==a:
        cnt += 1
print(cnt)