import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().strip().split()))

stack = [] # 오큰수를 구하지 못한 인덱스 스택
answer = [-1 for i in range(n)]

stack.append(0)
for i in range(1,n):
    while stack and arr[stack[-1]] < arr[i]: # 오큰수를 구하지 못한 수가 오큰수를 구할 때 동안
        answer[stack.pop()] = arr[i] # 답 넣기
    stack.append(i)
print(*answer)