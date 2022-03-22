from collections import deque

n = int(input())

cnt=0
arr = deque([])
for i in range(n,0,-1):
    arr.append(i)
    if sum(arr) == n:
        cnt+=1
    if sum(arr) >= n:
        arr.popleft()

print(cnt)