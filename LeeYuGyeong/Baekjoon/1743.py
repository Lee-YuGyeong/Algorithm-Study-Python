from collections import deque

def bfs(x,y):
    global maximum
    cnt =0
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        x,y = queue.popleft()
        cnt+=1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < N and 0<=ny<M:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    
    maximum = max(maximum,cnt)

N,M,K = map(int,input().split())
graph = [[0 for i in range(M)] for j in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

maximum=0

for _ in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs(i,j)

print(maximum)