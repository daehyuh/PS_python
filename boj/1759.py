from itertools import combinations
l, c = map(int, input().split())

alpha = list(input().split())
mo = ['a','e','i','o','u']
answer = []
result = list(combinations(alpha, l))

for i in result:
    i = list(i)
    i.sort()
    cnt = 0
    for j in i:
        if j in mo:
            cnt+=1
    if 1 <= cnt <= l - 2:
        ret = ''.join(i)
        answer.append(ret)

answer.sort()
for i in answer:
    print(i)