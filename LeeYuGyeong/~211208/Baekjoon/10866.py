from collections import deque
import sys
input=sys.stdin.readline
n = int(input())
q = deque([])
for _ in range(n):
    arr = input().split()
    if arr[0]=="push_front": q.appendleft(int(arr[1]))
    elif arr[0]=="push_back" : q.append(int(arr[1]))
    elif arr[0]=="pop_front" : print(q.popleft()) if q else print(-1)
    elif arr[0]=="pop_back" : print(q.pop()) if q else print(-1)
    elif arr[0]=="size" : print(len(q))
    elif arr[0]=="empty" : print(0) if q else print(1)
    elif arr[0]=="front" : print(q[0]) if q else print(-1)
    elif arr[0]=="back" : print(q[-1]) if q else print(-1)