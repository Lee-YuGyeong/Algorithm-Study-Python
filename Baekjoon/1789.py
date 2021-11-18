N = int(input())

i=1
sol=0
isSolve = False

while True:
    if N<i:
        isSolve = True
        break 
    if isSolve: break    
    N-=i
    i+=1
    sol+=1
    

print(sol)