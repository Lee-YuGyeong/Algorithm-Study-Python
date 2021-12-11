from collections import deque

n,m = map(int,input().split())
arr_ = deque(map(int,input().split())) #1
arr = deque([i+1 for i in range(n)]) #2
cnt=0
while arr_:
    x = arr.index(arr_[0]) #3
    if x<=len(arr)//2: #4
        arr.rotate(-x) #5
        cnt+=x
    else: #6
        arr.rotate(len(arr)-x)
        cnt+=len(arr)-x
    arr.popleft() #7
    arr_.popleft() #8
print(cnt)