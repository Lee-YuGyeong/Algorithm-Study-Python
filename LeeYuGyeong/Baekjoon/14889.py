import sys
input=sys.stdin.readline

def dfs():
    if len(s)==n//2:
        print(s)
        break
    for i in range(n):
        
        

arr=[]
s = []
n = int(input())
for _ in range(n):
    x = list(map(int,input().split()))
    arr.append(x)

mininum=100*n//2
visited=[False]*n
dfs(1)
print(mininum)