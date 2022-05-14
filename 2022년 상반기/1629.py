def go(a,b):
    if b==1: return a 
    sol = go(a,b//2) # 재귀 (이때 b//2로 해준다.) 
    sol = (sol*sol)%c # 곱해준다.
    if b%2: sol = (sol*a)%c # b가 홀수이면 한번 더 곱해야한다
    return sol%c

a,b,c = map(int,input().split())
print(go(a,b)%c)
