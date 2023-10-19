a, b, c = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()

arrSum = [arr[0]]
arrSaleSum = [arr[0] // 2]

for i in range(1, a):
    arrSum.append(arr[i] + arrSum[i - 1])
for i in range(1, a):
    arrSaleSum.append(arr[i] // 2 + arrSaleSum[i - 1])

start = 0
end = 0
cost = 0


for i in range(c):
    cost = arrSaleSum[i]
    if cost > b:
        break
    end += 1

while end < a:
    cost = arrSum[start] + (arrSaleSum[end]-arrSaleSum[start])
    if cost > b:
        break
    end += 1
    start += 1

print(end)