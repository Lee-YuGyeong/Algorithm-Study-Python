from itertools import product
a,b = map(int,input().split())
for i in product([i+1 for i in range(a)],repeat=b):
    print(*i)
