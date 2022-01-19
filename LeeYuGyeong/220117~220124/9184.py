d = [[[10**9 for _ in range(101)] for _ in range(101)] for _ in range(101)]

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        if d[a][b][c] != 10**9:
            return d[a][b][c]
        else:
            d[a][b][c] = w(20,20,20)
            return d[a][b][c]
    elif a<b<c:
        if d[a][b][c] != 10**9:
            return d[a][b][c]
        else:
            d[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
            return d[a][b][c]
    else:
        if d[a][b][c] != 10**9:
            return d[a][b][c]
        else:
            d[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
            return d[a][b][c]

while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    d[a][b][c] = w(a,b,c)
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,d[a][b][c]))