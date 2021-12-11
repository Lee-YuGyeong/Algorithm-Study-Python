import sys
input=sys.stdin.readline
n = int(input())
answer=[-1]*n
stack=[]
arr=[]
for idx,a in enumerate(input().split()):
    arr.append([int(a),idx])
i=0
for q in range(n):
    if stack and stack[-1][0] < arr[i][0]:
        for idx,s in enumerate(stack):
            if s[0]<arr[i][0]:
                for k in range(idx,len(stack)):
                    answer[stack[k][1]]=str(arr[i][0])
                stack = stack[:idx]
                break
        stack.append(arr[i])
        i+=1
    else:
        stack.append(arr[i])
        i+=1
for a in answer:
    sys.stdout.write(str(a)+" ")