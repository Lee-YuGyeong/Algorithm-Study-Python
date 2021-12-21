import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x==0:  print(heapq.heappop(h)[1]) if h else print(0)
    else: heapq.heappush(h,(-x,x))