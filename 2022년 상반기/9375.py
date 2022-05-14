import sys

n = int(input())
for i in range(n):
    dic = {}
    m = int(input())
    for j in range(m):
        x = sys.stdin.readline().strip().split()
        if x[1] in dic:
            dic[x[1]] +=1
        else:
            dic[x[1]] = 1
    sol = 1
    for col in dic:
        dic[col]
        sol *= dic[col] + 1
    print(sol-1)
    
