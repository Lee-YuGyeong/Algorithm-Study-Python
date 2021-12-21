n = int(input())

for _ in range(n):
    p = [0,1,1,1,2,2]
    x = int(input())
    for i in range(6,x+1):
        p.append(p[i-1] + p[i-5])
    print(p[x])