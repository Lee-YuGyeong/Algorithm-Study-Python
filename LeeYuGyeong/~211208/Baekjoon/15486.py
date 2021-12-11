import sys
N = int(input())
T = [0 for i in range(N+1)]
P = [0 for i in range(N+1)]
d = [[0,0] for i in range(N+1)]
for i in range(1,N+1):
    t,p = map(int,sys.stdin.readline().split())
    T[i] = t
    P[i] = p

for i in range(1,N+1):
    if T[i] + i -1 < N+1 and d[T[i] + i -1][1] == 0:
        d[T[i] + i -1][0] = max(max(d[1:d[T[i] + i]][0]),d[i][0]+P[i])
        d[T[i] + i -1][1] = 1
        print("1 : ",i,T[i] + i -1,d[T[i] + i -1][0])
    elif T[i] + i < N+1 and d[T[i] + i][1] == 0:
        max(max(d[1:d[T[i] + i]][0]),d[i][0]+P[i])
        d[T[i] + i][0] = max(d[T[i] + i][0],d[i][0]+P[i])
        d[T[i] + i][1] = 1
        print("2 : ",i,T[i] + i,d[T[i] + i][0])
print(d)
