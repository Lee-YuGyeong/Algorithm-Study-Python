n = int(input())
ss = list(input().split('*')) # *을 기준으로 나눠줌
for i in range(n):
    aa = input()
    if len(ss[0])+len(ss[1])<=len(aa): # 입력받은 문자열의 길이가 같거나 더 길어야함
        for a,b in zip(ss[0],aa): # * 앞에 있는 문자를 비교 
            if a!=b: # 다르면 NE 출력
                print('NE')
                break
        else: # 다른게 없었다면 
            for a,b in zip(ss[1][::-1],aa[::-1]): # * 뒤의 문자를 비교. 이때 문자를 뒤집어서 비교
                if a!=b: # 다르면 
                    print('NE') # NE 출력
                    break
            else:
                print('DA') # 다른게 없었다면 DA 출력
    else: # 입력받은 문자열의 길이가 더 짧으면 NE 출력
        print('NE')
    