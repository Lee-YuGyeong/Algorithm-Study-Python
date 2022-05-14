from collections import Counter
ss = list(input())

dic = Counter(ss) # 개수 세주기
cnt=1
answer=[]
one = ''
for d in dic:
    for i in range(dic[d]//2): # 반만큼 answer에 더하기
        answer.append(d)
    if dic[d]%2!=0: # 홀수일경우
        if cnt==2: # 홀수인게 한개가 넘을경우
            print("I'm Sorry Hansoo") # 실패
            break
        else:
            cnt+=1 # 홀수가 하나일경우
            one=d # 홀수 값 저장

else:
    answer.sort() # 사전순으로 정렬해주기
    print('%s%s%s'%(''.join(answer),one,''.join(answer[::-1]))) # 정렬된값 + 홀수 값 + 정렬 역순 값
    

    
    

    