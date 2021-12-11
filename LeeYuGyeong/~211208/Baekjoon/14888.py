import sys
from itertools import permutations

N = int(input())
num = list(map(int,sys.stdin.readline().split()))
tmp = list(map(int,sys.stdin.readline().split()))
arr = []
cnt=0
for i in tmp:
    cnt+=1
    for j in range(i):
        arr.append(cnt)

p = set(permutations(arr,len(arr)))
l = []
for tuple in p:
    sol=num[0]
    tmp=num[1:]
    for n,op in zip(tmp,tuple):
        if op == 1:
            sol+=n
        elif op == 2:
            sol-=n
        elif op==3:
            sol*=n
        else:
            if(sol<0):
                sol*=-1 
                sol//=n
                sol*=-1
            else:
                sol//=n
    l.append(sol)

print(max(l))
print(min(l))