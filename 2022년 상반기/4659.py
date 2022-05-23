dic = {'a','e','i','o','u'}

while True:
    ss = input()
    if ss == 'end': break
    check1 = False
    before1 = ['0',False] # 첫번째 전 (문자,모음 여부)
    before2 = ['0',False] # 두번째 전 (문자,모음 여부)
    now = ['0',False] # # 현재 (문자,모음 여부)
    for i,s in enumerate(ss):
        if s in dic:
            check1 = True # 1번 조건 체크
            now = [s,True]
        else:
            now = [s,False]

        if i >= 2: # 2번 조건 체크
            if before1[1] == before2[1] and before2[1] == now[1]: # 전, 전전, 현재 모음자음 여부 같은지 체크
                print("<%s> is not acceptable."%(ss)) # 같으면 not 출력
                break
        if i >= 1: # 3번 조건 체크
            if before1[0] == now[0]: # 전의 문자와 현재 문자 같으면
                if now[0] != 'e' and now[0] != 'o': # e와 o가 아니면
                    print("<%s> is not acceptable."%(ss))
                    break
        before2 = before1 # 전을 전전으로
        before1 = now # 현재를 전으로
    else:
        if check1:
            print("<%s> is acceptable."%(ss))
        else:
            print("<%s> is not acceptable."%(ss))
                

            