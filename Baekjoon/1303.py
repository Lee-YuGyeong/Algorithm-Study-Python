import sys
from collections import deque

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    
    cnt=0

    while queue:
        v = queue.popleft()
        cnt+=1
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
    return cnt

N,K = map(int,input().split())
arr=[]
for i in range(K):
    tmp=[]
    for color in sys.stdin.readline()[:-1]:
        tmp.append(color)
    arr.append(tmp)


graph = [[] for _ in range(K*N)]
visited = [False for _ in range(K*N)]

cnt=0
for i in range(K):
    cnt=i*N
    for j in range(N-1):
        if arr[i][j] == arr[i][j+1]:
            graph[cnt].append(cnt+1)
            graph[cnt+1].append(cnt)
        cnt+=1

cnt=0
for i in range(K-1):
    cnt=i*N
    for j in range(N):
        if arr[i][j] == arr[i+1][j]:
            graph[cnt].append(cnt+N)
            graph[cnt+N].append(cnt)
        cnt+=1

scoreW,scoreB = 0,0

for i in range(K*N):
    if visited[i] == False:
        score = bfs(graph,visited,i)
        if arr[i//N][i%N] == 'W':
            scoreW+=score**2
        else:
            scoreB+=score**2

print(scoreW,scoreB)
