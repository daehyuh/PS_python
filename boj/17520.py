from itertools import *
n = int(input())
printList = list(combination(['0', '1'], repeat=n))

cnt = 0
for i in printList:
    a = str(''.join(i))
    zero = a.count('0')
    one = a.count('1')
    print(a, zero, one)
    if 1 >= (max(zero, one) - min(zero, one)):
        print(a)
        cnt+=1
print(cnt)