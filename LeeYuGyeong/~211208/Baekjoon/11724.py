import sys
sys.setrecursionlimit(10000)

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
visited[0] = True
for _ in range(M):
    l,r = map(int,sys.stdin.readline().split())
    graph[l].append(r)
    graph[r].append(l)

cnt=0
for i in range(1,N+1):
    if visited[i] == False:
        dfs(graph,i,visited)
        cnt+=1

print(cnt)
