N,K = map(int,input().split())

arr = [i+1 for i in range(N)] #1
answer=[]
cur=0 #2
while arr: #3
    cur = (cur+K-1)%len(arr) #4
    answer.append(arr.pop(cur)) #5
print("<"+", ".join(map(str,answer))+">") #6