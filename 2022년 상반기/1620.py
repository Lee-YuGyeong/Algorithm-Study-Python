import sys
n,k = map(int,input().split())
dic = {}
for i in range(1,n+1):
    ss = sys.stdin.readline().strip()
    dic[str(i)] = ss
    dic[ss] = str(i)
for i in range(k):
    x = sys.stdin.readline().strip()
    print(dic[x])
