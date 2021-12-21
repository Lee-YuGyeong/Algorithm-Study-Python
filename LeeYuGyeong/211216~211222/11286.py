import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x: heapq.heappush(h,(abs(x),x))
    else:
        print(heapq.heappop(h)[1]) if h else print(0)