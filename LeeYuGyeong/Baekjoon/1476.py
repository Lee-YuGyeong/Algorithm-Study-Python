E,S,M = map(int,input().split())

cnt=0
while True:
    cnt+=1
    e,m,s = cnt%15,cnt%19,cnt%28
    if e == 0: e=15
    if m == 0: m=19
    if s == 0: s=28
    if e==E and m==M and s==S:
        print(cnt)
        break
