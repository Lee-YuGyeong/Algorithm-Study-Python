import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = int(input())
    cnt=0
    i=5
    while i<=x: # 5가 몇개가 들어가는지 구해준다.
        cnt+=x//i
        i*=5
    print(cnt)