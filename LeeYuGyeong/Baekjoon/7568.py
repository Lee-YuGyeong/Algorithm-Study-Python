import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

for w,h in arr:
    cnt=0
    for tmp_w,tmp_h in arr:
        if tmp_w > w and tmp_h > h:
            cnt+=1
    print(cnt+1,end=" ")     