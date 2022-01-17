import sys
input = sys.stdin.readline

n = int(input())
t = []
for _ in range(n):
    a,b = map(int,input().split())
    t.append([a,b])
end,cnt=0,0
for a,b in sorted(t,key=lambda x:(x[1],x[0])):
    if end <= a:
        cnt+=1
        end = b
print(cnt)