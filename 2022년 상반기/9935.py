ss = input()
m = list(input())

stack = []

for i in range(len(ss)):
    stack.append(ss[i]) # 스택에 하나씩 추가
    if stack[-len(m):] == m: # 스택의 마지막이 m 문자열과 같으면
        del stack[-len(m):] # 삭제

if stack: print("".join(stack))
else: print("FRULA")