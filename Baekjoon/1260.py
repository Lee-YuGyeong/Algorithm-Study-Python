from collections import deque

def dfs(graph,n,visited):
    
    visited[n] = True
    print(n,end=" ")

    for i in graph[n]:
        if visited[i] == False:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if visited[i]==False:
                visited[i] = True
                queue.append(i)


N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(M):
    l,r = map(int,input().split())
    graph[l].append(r)
    graph[r].append(l)

[g.sort() for g in graph]

dfs(graph,V,visited)
visited = [False for _ in range(N+1)]
print()
bfs(graph,V,visited)

