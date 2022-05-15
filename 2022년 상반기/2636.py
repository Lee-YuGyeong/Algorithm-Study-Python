from collections import deque
import queue
import sys
import copy

n,m = map(int,input().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 치즈녹이기
def melt():

    global n,m

    tmp_arr = copy.deepcopy(arr)

    for i in range(n):
        for j in range(m):
            
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0<=nx<n and 0<=ny<m and air[nx][ny]==True:
                    arr[i][j] = 0
                    break


    return arr

# 밀폐된 공기 빼고 구하기
def bfs():
    queue = deque([])
    queue.append([0,0])
    air[0][0] = True

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0 and air[nx][ny] == False:
                    air[nx][ny] = True
                    queue.append([nx,ny])
    


cnt=0
answer=[]
c=0
for i in range(n):
    c+=arr[i].count(1)
answer.append(c)
while True:

    air = [[False]*m for _ in range(n)]

    bfs()

    arr = melt()
    cnt+=1
    c = 0
    for i in range(n):
        c+=arr[i].count(1)
    answer.append(c)
    if c==0: break

print(cnt)
print(answer[-2])
    