import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    return graph[N-1][M-1]

N,M = map(int,input().split())
graph = [list(map(int,sys.stdin.readline()[:-1])) for _ in range(N)]

dx = [0,1,-1,0]
dy = [1,0,0,-1]

print(bfs(0,0))