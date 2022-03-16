ss = input().split('.') # .으로 나눠줌
sol_str = ''
for x in ss:
    if len(x) % 2 == 1: # 홀수면 덮을 수 없음
        print(-1)
        break
    while len(x) >= 4: # 4보다 크면 AAAA 덮기
        sol_str+='AAAA'
        x = x[4:]
    if len(x) == 2: # 2가 남았으면 BB 덮기
        sol_str+='BB'
        x = x[2:]
    sol_str+='.' # 나눠준 . 붙이기
else:
    print(sol_str[:-1]) # 성공이면 마지막 . 제외하고 출력
    