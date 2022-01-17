from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    queue = deque([[x,y]])
    graph[x][y] = 0

    while queue:
        a,b = queue[0][0], queue[0][1]
        queue.popleft()
        for i in range(4):
            cx = a + dx[i]
            cy = b + dy[i]
            if 0<=cx<n and 0<=cy<m and graph[cx][cy] == 1:
                graph[cx][cy] = 0
                queue.append([cx,cy])


n = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    cnt=0
    for j in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt+=1
    print(cnt)
