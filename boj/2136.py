n = int(input())
l = list(map(int, input().split(' ')))
l.sort()
s = 0
e = n - 1

temp = abs(l[s] + l[e])
final = [l[s], l[e]]

while s < e:
    if abs(l[s] + l[e]) < temp:
        temp = abs(l[s] + l[e])
        final = [l[s], l[e]]
        if temp == 0:
            break
    if l[s] + l[e] < 0:
        s += 1
    else:
        e -= 1

print(final[0], final[1])