arr = []
arr2 = []
for i in range(3):
    arr.append(int(input()))
for i in range(2):
    arr2.append(int(input()))
arr.sort()
arr2.sort()
print(arr[0]+arr2[0]-50)