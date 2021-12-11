import sys
from collections import deque
input = sys.stdin.readline
 
def bfs(x, y, color):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
 
    while queue:
        x, y = queue.popleft()
        print("x y : ",x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print("nx ny : ",nx,ny)
            if 0 <= nx < m and 0 <= ny < n:
                print("범위 안 nx ny : ",nx,ny)
                if graph[nx][ny] == color and not visited[nx][ny]:    # each color check
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1    # each color count
                    print(cnt)
 
    return cnt + 1
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[False] * n for i in range(m)]

print(graph)
white, blue = 0, 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2    # count accumulate
            print("bfs(i, j, 'W')",bfs(i, j, 'W'))
        elif graph[i][j] == 'B' and not visited[i][j] :
            blue += bfs(i, j, 'B') ** 2    # count accumulate
 
print(white, blue)