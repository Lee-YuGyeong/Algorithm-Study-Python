from itertools import combinations

N,M = map(int,input().split())
arr = list(map(int,input().split()))

maximum = 0
for com in combinations(arr,3):
    if sum(com) <= M:
        maximum = max(maximum,sum(com))
print(maximum)