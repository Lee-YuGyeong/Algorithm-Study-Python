from collections import deque

n = int(input())
q = deque([i+1 for i in range(n)])
for i in range(n-1):
    q.popleft()
    q.rotate(-1)
print(q[0])