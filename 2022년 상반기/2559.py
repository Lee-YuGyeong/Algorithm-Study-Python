n,k = map(int,input().split())
arr = list(map(int,input().split()))
num = 0
cnt=0
answer=[]
for i in range(len(arr)):
    num+=arr[i]
    cnt+=1
    if cnt == k:
        cnt-=1
        answer.append(num)
        num-=arr[i-k+1]
print(max(answer))