import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def upper_bound(x): # 타겟보다 큰 값이 나오는 처음 위치
    start,end=0,len(arr1)
    while start<end:
        mid = (start + end) //2
        if arr1[mid] <= x:
            start = mid + 1
        else:
            end = mid
    return end

def lower_bound(x): # 타겟과 같은 값이 나오는 처음 위치, 만약 같은 값이 없는 경우에는 타겟보다 큰 값이 나오는 처음 위치
    start,end=0,len(arr1)
    while start<end:
        mid = (start + end) //2
        if arr1[mid] < x:
            start = mid + 1
        else:
            end = mid
    return end

sol=[]
for i in arr2:
    sol.append(upper_bound(i)-lower_bound(i))
print(*sol)
    
