n,k = map(int,input().split())
arr = []
cnt=0
for _ in range(n):
    arr.append(int(input()))

for i in sorted(arr,reverse=True):
    if k >= i :
        cnt+=k//i
        k=k%i
print(cnt)
