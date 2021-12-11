from collections import deque
import sys
input=sys.stdin.readline

n = int(input())
for _ in range(n):
    a,b=map(int,input().split())
    arr = deque(map(int,input().split()))
    index=b #1
    cnt=0
    while True:
        x = arr.popleft() #2
        if not arr: # 3
            print(cnt+1)
            break
        if x < max(arr): #4
            arr.append(x)
            if index==0: index=len(arr)-1
            else: index-=1
            
        else: 
            if index==0: #5 
                print(cnt+1)
                break
            else: #6
                cnt+=1
                index-=1
            