import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(input()[:-1]) for _ in range(N)]
color=['W','B']
minimum = 64
for i in range(N):
    for j in range(M):
        sum_w,sum_b=0,0
        if i+8<=N and j+8<=M:
            for l in range(i,i+8):
                for k in range(j,j+8):
                    color_idx = (l%2+k)%2
                    if arr[l][k] != color[color_idx]: sum_w+=1
                    if arr[l][k] == color[color_idx]: sum_b+=1
            minimum = min(minimum,sum_w,sum_b)

print(minimum)