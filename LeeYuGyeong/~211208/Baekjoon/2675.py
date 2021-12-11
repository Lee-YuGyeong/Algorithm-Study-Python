n = int(input())

for _ in range(n):
    a,b = input().split()
    answer=""
    for i in list(b):
        answer+=i*int(a)
    print(answer)
        