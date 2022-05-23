import sys
n = int(input())
arr = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]

def tree(x,y,n):
    check = arr[x][y] # 체크할 기준 설정
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != arr[i][j]: # 다른게 있으면
                check = -1 # 다르다고 체크
                break
    if check == -1: # 다르면 쪼개기
        print("(",end="")
        n//=2
        tree(x,y,n) # 왼쪽 위
        tree(x,y+n,n) # 오른쪽 위
        tree(x+n,y,n) # 왼쪽 아래
        tree(x+n,y+n,n) # 오른쪽 아래
        print(")",end="")
    elif check == 0:
        print("0",end="")
    else:
        print("1",end="")

tree(0,0,n)