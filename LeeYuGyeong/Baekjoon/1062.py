from itertools import combinations

N,K = map(int,input().split())

arr = ["0" for i in range(N)]

for i in range(N):
    tmp = input()
    arr[i] = tmp

sol=False

for i in range(N,0,-1):
    com = list(combinations(arr,i))
    for j in com:
        s = set()
        for k in j:
            for l in k:
                s.add(l)
        if len(s) <= K:
           sol=True
           print(len(j))
           break
    if sol==True:break
if sol==False: print(0)


