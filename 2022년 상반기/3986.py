import sys
n = int(input())
cnt=0
for _ in range(n):
    stack = []
    ss = list(sys.stdin.readline().strip())
    for i in range(len(ss)):
        if not stack or stack[-1] != ss[i]:
            stack.append(ss[i])
        elif stack[-1] == ss[i]:
            stack.pop(-1)
    if not stack :
        cnt+=1
print(cnt)
