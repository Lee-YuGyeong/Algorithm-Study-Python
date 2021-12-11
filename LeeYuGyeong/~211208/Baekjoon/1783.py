cnt=[0,0,0,0]
N,M = map(int,input().split())

cx,cy = 1,1

while True:
    if cx==M or cy==N: 
        break
    y = N-cy
    x = M-cx
    if x<y:
        if 3<=cy:
            cnt[3]+=1
            cx+=1
            cy-=2
        else:
            cnt[0]+=1
            cx+=1
            cy+=2
    else:
        if 2<=cy:
            cnt[2]+=1
            cx+=2
            cy-=1
        else:
            cnt[1]+=1
            cx+=2
            cy+=1

if sum(cnt)>=4:
    cnt[0]-=2
    cnt[1]+=1
if sum(cnt)>=4:
    cnt[3]-=2
    cnt[2]+=1
print(sum(cnt)+1)


