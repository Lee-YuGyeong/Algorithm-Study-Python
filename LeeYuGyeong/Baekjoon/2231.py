n = int(input())
cnt=0
while True:
    cnt+=1
    if sum(list(map(int,str(cnt))))+cnt == n:
        print(cnt)
        break
    if cnt==n: 
        print(0)
        break