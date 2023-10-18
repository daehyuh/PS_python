n = int(input())

arr = list(map(int, input().split()))

avg = sum(arr) // n

sum1 = 0
sum2 = 0

for i in arr:
    if i > (avg+1):
        sum1 += (i - avg - 1)
    elif i < avg:
        sum2 += (avg - i)
print(max(sum1, sum2))

