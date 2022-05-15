import queue
import sys
from collections import deque

m,n,k = map(int,input().split())
arr = [[0]*n for _ in range(m)]

for _ in range(k):
    a,b,c,d = map(int,sys.stdin.readline().strip().split())
    for i in range(b,d):
        for j in range(a,c):
            arr[i][j] = 1

visited = [[False]*n for _ in range(m)]
sol = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    queue = deque([])
    queue.append([i,j])
    visited[i][j] = True
    cnt=1

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for node in range(4):
            node_x = dx[node] + x
            node_y = dy[node] + y
            if 0<=node_x<m and 0<=node_y<n and visited[node_x][node_y] == False and arr[node_x][node_y] == 0:
                cnt+=1
                visited[node_x][node_y] = True
                queue.append([node_x,node_y])
    return cnt

for i in range(m):
    for j in range(n):
        if visited[i][j] == False and arr[i][j] == 0:
            sol.append(bfs(i,j))
print(len(sol))
print(*sorted(sol))


    
    

