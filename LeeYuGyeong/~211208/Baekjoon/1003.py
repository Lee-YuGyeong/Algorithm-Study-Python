def fibonacci(n):
    global cnt_0,cnt_1
    if n==0:
        cnt_0+=1
        return 0
    elif n==1:
        cnt_1+=1
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = int(input())
d=[0]*n
d[0]=0
d[1]=1
for j in range(2,n):
    if 
for i in range(n):
    cnt_0,cnt_1=0,0
    x = int(input())
    fibonacci(x)
    print(cnt_0,cnt_1)


