n = int(input())
arr = list(map(int,input().split()))

cnt=0
while any(arr): # arr 에 1 이상이 하나라도 있을 경우 반복
    tmp = [i for i in arr] # 2로 나누어질 경우 저장
    for i in range(len(arr)):
        if arr[i] %2 ==0 : # 만약 2로 나눠지면
            tmp[i] = arr[i]//2 # tmp에 2로 나눈 결과 저장
        else: #나눠지지 않으면
            arr[i]-=1 # 1을 뺌
            cnt+=1
            break
    else: # 모두 2로 나누어지면 arr에 tmp 대입
        arr = tmp
        cnt+=1

print(cnt)
    
