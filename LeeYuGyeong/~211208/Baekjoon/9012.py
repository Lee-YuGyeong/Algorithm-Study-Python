import sys
input=sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(input()[:-1])
    s = []
    for a in arr:
        if a=='(':
            s.append(a)
        else:
            if len(s) :s.pop()
            else:
                print("NO")
                break
    else:
        print("NO") if len(s) else print("YES")
        