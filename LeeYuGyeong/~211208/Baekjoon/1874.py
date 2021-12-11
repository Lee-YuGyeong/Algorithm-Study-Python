n=int(input())
arr,s,answer=[],[],[]
for i in range(n):
    x = int(input())
    arr.append(x)
sol=False
i=0
while True:
    if not arr and not s:
        sol=True
        break
    if i==n and s and arr[0] != s[-1]:
        sol=False
        break
    if s and arr[0] == s[-1]:
        arr.pop(0)
        s.pop()
        answer.append("-")
    else:
        i+=1
        s.append(i)
        answer.append("+")
print('\n'.join(answer)) if sol else print("NO")