import sys
r,c,t = map(int,input().split())

arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(r)]

# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i+1
        break

# 미세먼지 확산
def dust():
    di = [1,0,-1,0] # 하,우,상,좌
    dj = [0,1,0,-1]
    tmpArr = [[0]*c for j in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j]>=5:
                cnt=0
                for k in range(4):
                    x = di[k]+i
                    y = dj[k]+j
                    if 0<=x<r and 0<=y<c and arr[x][y] != -1:
                        tmpArr[x][y] += arr[i][j]//5 
                        cnt+=1
                tmpArr[i][j] -= arr[i][j]//5*cnt
    for i in range(r):
        for j in range(c):
            arr[i][j] = arr[i][j] + tmpArr[i][j]


# 공기 청정기 위쪽 이동
def air_up():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    direct = 0
    before = 0
    x,y = up,1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if not 0 <= nx < r or not 0<= ny < c:
            direct += 1
            continue
        arr[x][y],before = before,arr[x][y]
        x = nx
        y = ny

# 공기 청정기 아래쪽 이동
def air_down():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    direct = 0
    before = 0
    x,y = down,1
    while True:
        nx = dx[direct] + x
        ny = dy[direct] + y
        if x == down and y == 0:
            break
        if not 0<=nx<r or not 0<=ny<c:
            direct+=1
            continue
        arr[x][y],before = before,arr[x][y]
        x = nx
        y = ny

for _ in range(t):
    dust()
    air_up()
    air_down()


sol = 0
for i in range(r):
    for j in range(c):
        sol+=arr[i][j]
print(sol+2)



