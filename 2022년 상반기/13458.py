n = int(input())
arr = map(int,input().split())
b,c = map(int,input().split())

sol = 0
for i in arr:
    sol +=1
    i = i-b
    if i>0: 
        sol+=i//c
        if i%c !=0 : sol+=1
print(sol)
