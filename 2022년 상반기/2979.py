a,b,c = map(int,input().split())

arr = []
time = [0 for i in range(100)]

for i in range(3):
    x,y = map(int,input().split())
    for j in range(x,y):
        time[j-1]+=1

sol = 0
for i in range(len(time)):
    if time[i] == 1:
        sol+=a
    elif time[i] == 2:
        sol+=b*2
    elif time[i] == 3:
        sol+=c*3
    else:
        continue
print(sol)

