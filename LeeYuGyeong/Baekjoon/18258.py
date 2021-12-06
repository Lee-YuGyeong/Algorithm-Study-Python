from collections import deque
import sys
input=sys.stdin.readline
queue=deque([])
n = int(input())
for i in range(n):
    arr = input().split()
    if arr[0]=="push": queue.append(arr[1])
    elif arr[0]=="pop": print(queue.popleft()) if queue else print(-1)
    elif arr[0]=="size": print(len(queue))
    elif arr[0]=="empty": print(0) if queue else print(1)
    elif arr[0]=="front": print(queue[0]) if queue else print(-1)
    else: print(queue[-1]) if queue else print(-1)