import sys
input=sys.stdin.readline

while True:
    arr = input()[:-1]
    if arr=='.': 
        break  
    else: arr=list(arr)
    stack=[]
    for idx in arr:
        if idx=='(' or idx=='[':
            stack.append(idx)
        elif idx==')':
            if len(stack) and stack[-1]=='(':
                stack.pop()
            else:
                print("no")
                break
        elif idx==']':
            if len(stack) and stack[-1]=='[':
                stack.pop()
            else:
                print("no")
                break
    else:
        print("no") if len(stack) else print("yes")