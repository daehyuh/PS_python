ans = 0
cnt = 0
for i in range(5):
    a = int(input())
    if a >= 40:
        cnt+=1
        ans+=a
    else:
        cnt+=1
        ans+=40
print(int(ans/cnt))