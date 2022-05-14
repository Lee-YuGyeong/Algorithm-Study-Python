n,m = map(int,input().split())

train = [[0 for _ in range(20)] for _ in range(n)]

for i in range(m):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        train[arr[1]-1][arr[2]-1] = 1
    elif arr[0]==2:
        train[arr[1]-1][arr[2]-1] = 0
    elif arr[0]==3:
        train[arr[1]-1].insert(0,0)
        train[arr[1]-1].pop()
    else:
        train[arr[1]-1].pop(0)
        train[arr[1]-1].append(0)

tmp = []
for t in train:
    if t not in tmp:
        tmp.append(t)
print(len(tmp))