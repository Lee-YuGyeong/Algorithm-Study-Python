import sys

def check(N,arr):
    maximum=1
    for i in range(N-1):
        row,col=1,1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                row+=1
            else:
                maximum = max(maximum,row)
                row=1

            if arr[j][i] == arr[j+1][i]:
                ##print(arr[j][i])
                col+=1
            else:
                maximum = max(maximum,col)
                col=1
            print(arr)
            
            print(i , " ",j , " ",row , " ",col , " ")
    return maximum

N = int(input())
arr=[]

for i in range(N):
    tmp=[]
    for i in sys.stdin.readline()[:-1]:
        tmp.append(i)
    arr.append(tmp)

for i in range(N):
    for j in range(N):
        if j<N-1:
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
            num = check(N,arr)
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
        if i<N-1:
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
            num = check(N,arr)
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
print(num)