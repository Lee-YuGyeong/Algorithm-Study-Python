import sys
input=sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
for i in sorted(arr):
    print(i)