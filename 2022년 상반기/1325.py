from collections import deque

n, m = map(int,input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

def bfs(graph,start):
    cnt=0
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.pop()
        cnt+=1
        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return cnt

maxinum = 0
sol = []
for i in range(1,n+1):
    visited = [False for i in range(n+1)]
    if len(graph[i])!=0:
        cnt = bfs(graph,i)
        visited[i] = cnt
        if maxinum < cnt:
            maxinum = cnt
            sol = [i]
        elif maxinum == cnt:
            sol.append(i)

print(*sol)
    
