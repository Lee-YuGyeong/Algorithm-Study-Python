n = int(input())
arr = list(input().split())
num = [False]*10

sol = []
answer = []

def dfs(cnt):

    if cnt==n:
        answer.append(''.join(map(str,sol))) # 숫자 다 넣었으면 answer에 추가
        return

    for i in range(10): # 두번째 숫자부터 부등호 비교
        if num[i] == False: # 사용하지 않은 숫자라면
            check = False
            if arr[cnt] == '<' and sol[-1] < i: # 등호 유효한지 체크
                check = True
            elif arr[cnt] == '>' and sol[-1] > i: # 등호 유효한지 체크
                check = True
            if check: # 등호가 유효하면
                num[i] = True
                sol.append(i)

                dfs(cnt+1) # 재귀

                num[i] = False
                sol.pop()

for i in range(10): # 첫 숫자 넣어주기
    num[i] = True
    sol.append(i)
    dfs(0)
    num[i] = False
    sol.pop()

print(answer[-1]) 
print(answer[0])    