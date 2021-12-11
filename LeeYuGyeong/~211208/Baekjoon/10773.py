n = int(input())
a = []
for _ in range(n):
    x = int(input())
    a.pop() if x==0 else a.append(x)
print(sum(a))