def dfs(x): # 전에 방문한 노드보다 큰 노드만 방문하기 위해 파라미터로 전달
    if len(s)==b: # 만약 s의 길이가 구해야하는 길이와 같으면 
        print(*s) # 출력하고 멈춘다
        return

    for i in range(x+1,a+1): # 전에 방문한 노드 +1 부터 반복 
        visited[i] = True # 방문했으므로 true로 바꿈
        s.append(i) # 방문한 노드를 s에 추가한다
        dfs(i) # 방문한 노드를 파라미터로 전달하여 이것보다 큰 것만 방문하게 한다
        s.pop() # 전 상태로 돌리기 위해 pop()
        visited[i] = False # 전 상태로 돌리고 방문하지 않았다고 표시

s = [] # 답을 넣을 리스트를 만든다
a,b=map(int,input().split())
arr = [i for i in range(1,a+1)]
visited = [False] * (a+1)
dfs(0)