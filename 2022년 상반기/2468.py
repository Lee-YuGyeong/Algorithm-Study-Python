import sys
from collections import deque

n = int(input())

maxinum = 0 # 가장 높은 지역 높이
arr = []
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    arr.append(tmp)
    maxinum = max(maxinum,max(tmp))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 안전한 지역 구하기
def bfs(i,j,area,visited):
    queue = deque([])
    queue.append([i,j])
    visited[i][j] = True

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0<=x<n and 0<=y<n and visited[x][y] == False and area[x][y] != 0:
                visited[x][y] = True
                queue.append([x,y])
    

# 침수
def water(arr,l):
    tmp = [[1]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <=l:
                tmp[i][j] = 0
    return tmp

# 안전 영역 최댓값 구하기
sol=0
for k in range(maxinum):
    area = water(arr,k)
    visited = [[False]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if area[i][j] !=0 and visited[i][j] == False:
                bfs(i,j,area,visited)
                cnt+=1

    sol = max(sol,cnt)
print(sol)
                
