arr = list(input())
bar = 0
cnt = 0
i = 0

while True:
    if i==len(arr)-1: break
    if arr[i]=='(':
        if arr[i+1]==')':
            cnt+=bar
            i+=2
            continue
        bar+=1
        cnt+=1
    else:
        bar-=1
    i+=1
print(cnt)