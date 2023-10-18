a, b, c = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()

arrSum = [arr[0]]

for i in range(1, a):
    arrSum.append(arr[i] + arrSum[i - 1])
start = 0
reslist = []

while True:
    res = 0
    if start <= 2 or start <= c:
        res += arrSum[start] / 2
    else:
        res += arrSum[start - c]
        for i in range(start - c, start):
            res += arr[i] / 2
    if res <= b:
        reslist.append(start + 1)
    # print(reslist)
    start += 1
    if start == a:
        break

print(max(reslist))
