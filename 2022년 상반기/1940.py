n = int(input())
m = int(input())
arr = list(map(int,input().split()))
cnt=0
arr.sort()
left = 0
right = len(arr)-1
while left < right:
    if arr[left] + arr[right] == m:
        cnt+=1
        left+=1
        right-=1
    elif arr[left] + arr[right] >= m:
        right-=1
    else:
        left+=1
print(cnt)
