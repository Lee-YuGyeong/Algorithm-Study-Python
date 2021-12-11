import sys
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    x=input().split()
    if x[0]=="push": a.append(x[1])
    elif x[0]=="pop": print(-1 if len(a)==0 else a.pop())
    elif x[0]=="size":print(len(a))
    elif x[0]=="empty":print(1 if len(a)==0 else 0)
    elif x[0]=="top": print(-1 if len(a)==0 else a[-1])