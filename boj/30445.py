HAPPY = ['H', 'A', 'P', 'Y']
SAD = ['S', 'A', 'D']
n = input()
h = 0
s = 0
for i in n:
    if i in HAPPY:
        h+=1
    if i in SAD:
        s+=1
if h == s:
    print('50.00')
else:
    print((h/h+s)*10)