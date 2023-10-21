L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
aa = A//C
A = A%C
bb = B//D
B = B%D
if A != 0:
    aa+=1
if B !=0:
    bb+=1

print(L-max(aa, bb))