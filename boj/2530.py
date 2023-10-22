t, m, s = map(int, input().split())
o = int(input())

t+= o//3600
o %= 3600
m+= o//60
o %= 60
s += o

if s >= 60:
    m += s // 60
    s %= 60

if m >= 60:
    t += m // 60
    m %= 60

if t >= 24:
    t %= 24

print(t, m ,s)