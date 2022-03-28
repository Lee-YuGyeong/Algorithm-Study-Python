n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr2 = []
sol = -101
for i in arr:
    arr2.append(i)
    if len(arr2) == m: # 리스트에 k일 온도가 있으면
        sol = max(sol,sum(arr2)) # 최댓값 비교
        arr2.pop(0) 
print(sol)