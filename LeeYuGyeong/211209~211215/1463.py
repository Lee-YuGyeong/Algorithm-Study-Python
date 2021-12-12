n = int(input())

d=[0]*(n+1)
d[1]=0
for i in range(2,n+1):
    arr=[]
    if i%3==0:arr.append(d[i//3]+1)
    if i%2==0:arr.append(d[i//2]+1)
    arr.append(d[i-1]+1)
    d[i] = min(arr)
print(d[n])