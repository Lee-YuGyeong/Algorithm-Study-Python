import sys
input = sys.stdin.readline
n = int(input())
arr = [input()[:-1] for _ in range(n)]
arr = list(set(arr))
arr = sorted(arr,key=lambda x:(len(x),x))
for i in arr:
    print(i)