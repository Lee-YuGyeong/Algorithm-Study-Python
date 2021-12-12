import sys
input = sys.stdin.readline

def dfs(i,j):
    visited[i][j] = True # 방문한 곳을 True로 바꾸기
    cnt[-1]+=1 # 바꾸고 cnt 1 증가

    for p in range(4): # 상하좌우로 방문
        cx = d[p][0] + i 
        cy = d[p][1] + j
        if 0<= cx < N and 0 <= cy < N: # 계산한 좌표가 범위안이면
            if arr[cx][cy]=='1' and visited[cx][cy]==False: # cx,cy의 arr 이 1 이고 아직 방문하지 않았다면
                dfs(cx,cy) # 탐색
                    

arr,cnt,visited=[],[],[]
d = [[0,1],[1,0],[-1,0],[0,-1]] #상하좌우

N = int(input())
for _ in range(N):
    arr.append(list(input()[:-1]))
    visited.append([False]*N)

for i in range(N):
    for j in range(N):
        if arr[i][j]=="1" and visited[i][j]==False: # 1이면서 방문하지 않은곳이면
            cnt.append(0) # 
            dfs(i,j) # 탐색하기

print(len(cnt))
print("\n".join(map(str,sorted(cnt))))