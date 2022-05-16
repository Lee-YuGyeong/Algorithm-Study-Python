import sys
n = int(input())
arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


visited = [[False]*n for _ in range(n)]

sol = 201*n*n

def flower(cnt,c):

    global sol

    if cnt==3: # 3개 심어지면 최솟값 구하기
        sol = min(sol,c)
        return 
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                for k in range(4):
                    x = dx[k] + i
                    y = dy[k] + j
                    if not 0<=x<n or not 0<=y<n or not visited[x][y] == False: # 꽃을 심을 수 있으면
                        break
                else:
                    visited[i][j] = True
                    cost = arr[i][j]
                    for k in range(4):
                        x = dx[k] + i
                        y = dy[k] + j
                        visited[x][y] = True  
                        cost += arr[x][y]
                    flower(cnt+1,c+cost) # 꽃 1개 심기

                    visited[i][j] = False
                    for k in range(4):
                        x = dx[k] + i
                        y = dy[k] + j
                        visited[x][y] = False   

flower(0,0)
print(sol)