from collections import deque

n,m = map(int,input().split())
arr = []
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(arr,x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            node_x = x + dx[i]
            node_y = y + dy[i]
            if 0<= node_x < n and 0<= node_y < m:
                if visited[node_x][node_y] == False and arr[node_x][node_y] != 0:
                    queue.append([node_x,node_y])
                    visited[node_x][node_y] = True
                elif arr[node_x][node_y] == 0:
                    count[x][y] += 1
    return 1


year = 0
check_0 = False
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []

    # 빙산 개수 확인
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0 and visited[i][j] == False:
                result.append(bfs(arr,i,j))
    if len(result) == 0: # 빙산이 없으면
        check_0 = True 
        break
    elif len(result) >= 2: # 빙산이 2개 이상이면
        break

    # 빙산 녹임
    for i in range(n):
        for j in range(m):
            arr[i][j] -= count[i][j]
            if arr[i][j] < 0 : arr[i][j] = 0
    year+=1

if check_0: print(0)
else: print(year)

            