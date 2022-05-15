import sys
from collections import deque
import copy

n,m = map(int,input().split())

arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def makeWall(cnt): # 완전탐색으로 벽을 세움

    if cnt==3: # 벽 3개 세웠으면 bfs
        bfs()
        return 

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeWall(cnt+1)
                arr[i][j] = 0
            
def bfs():
    queue = deque([])
    tmp_arr = copy.deepcopy(arr) # 깊은 복사 (원래의 배열에 영향 안미침)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2: # 바이러스면 queue에 더하기
                queue.append([i,j])

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                queue.append([nx,ny])

    global answer

    cnt = 0
    for i in range(n): # 안전영역 계산
        cnt+=tmp_arr[i].count(0)
    
    answer = max(answer,cnt) # 최댓값 계산

answer=0
makeWall(0)

print(answer)
