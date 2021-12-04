import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    cnt=0
    while queue:
        v = queue.popleft()
        cnt+=1
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return cnt

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1)-1)
