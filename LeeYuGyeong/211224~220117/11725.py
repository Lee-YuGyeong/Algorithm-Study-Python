import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    global parents,tree
    for i in tree[node]: # tree[node](node의 부모 or 자식) 을 순회  
        if parents[i] == 0: # 만약 i의 부모가 아직 지정되지 않았다면
            parents[i] = node # node의 자식이므로 i의 부모를 node로 설정
            dfs(i) # i를 부모로 가진 노드를 찾기위해 dfs 탐색

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1): # 간선만큼 반복
    a,b = map(int,input().split()) # 부모, 자식 입력받아서
    tree[a].append(b) # 리스트에 넣기
    tree[b].append(a)

parents = [0 for _ in range(n+1)] # 부모 리스트 만들기
parents[1] = 1 # 1의 부모는 1로 설정

dfs(1) # 부모 찾기

print(*parents[2:])