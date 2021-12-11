h,w = input().split()
h,w = int(h),int(w)

x = input().split()
x = [h - int(i) for i in x]
arr = [[0 for i in range(w)]for j in range(h)]

for i in range(h):
    for j in range(w):
        if x[j] <= i:
            arr[i][j] = 1

cnt=0
for i in range(h-1,-1,-1):
    while True:
        if 0 not in arr[i]:
            i-=1
        else:
            break
    if arr[i].count(1) >=2:
        for j in range(arr[i].index(1)+1,len(arr[i]) - 1 - list(reversed(arr[i])).index(1)):
            if arr[i][j] == 0:
                cnt+=1
                arr[i][j] =1
print(cnt)




