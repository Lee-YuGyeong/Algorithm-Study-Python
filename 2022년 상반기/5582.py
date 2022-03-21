a = input()
b = input()

d = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
m = 0
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            d[i][j] = d[i-1][j-1] + 1
            m = max(m,d[i][j])

print(m)



