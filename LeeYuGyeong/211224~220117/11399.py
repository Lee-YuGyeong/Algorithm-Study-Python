n = int(input())
arr = list(map(int,input().split()))
t = 0
arr.sort()
for i in range(len(arr)):
    t += sum(arr[:i+1])
print(t)